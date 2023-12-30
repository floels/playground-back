import os
import boto3
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from pinit_api.models import Pin, Account
from pinit_api.utils.constants import (
    ERROR_CODE_PIN_CREATION_FAILED,
    ERROR_CODE_MISSING_PIN_IMAGE_FILE,
    ERROR_CODE_MISSING_USERNAME,
    ERROR_CODE_WRONG_USERNAME,
)
from pinit_api.tests.testing_utils import AccountFactory
from pinit_api.serializers.pin_serializers import PinBasicReadSerializer


def compute_file_key_s3(pin_id, extension):
    return f"pins/pin_{pin_id}{extension}"


def compute_file_url_s3(file_key_s3):
    return f"https://{settings.S3_PINS_BUCKET_URL}/{file_key_s3}"


def upload_file_to_s3(file, file_name):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.S3_PINS_BUCKET_UPLOADER_ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3_PINS_BUCKET_UPLOADER_SECRET_ACCESS_KEY,
    )

    s3_client.upload_fileobj(file, settings.S3_PINS_BUCKET_NAME, file_name)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_pin(request):
    username = request.META.get("HTTP_X_USERNAME")

    if not username:
        response_data = {"errors": [{"code": ERROR_CODE_MISSING_USERNAME}]}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    user = request.user

    account = Account.objects.filter(username=username, owner=user).first()

    if not account:
        response_data = {"errors": [{"code": ERROR_CODE_WRONG_USERNAME}]}
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)

    title = request.data.get("title")
    description = request.data.get("description")
    uploaded_file = request.FILES.get("image_file")

    if not uploaded_file:
        response_data = {"errors": [{"code": ERROR_CODE_MISSING_PIN_IMAGE_FILE}]}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    pin = Pin.objects.create(title=title, description=description, author=account)

    _, uploaded_file_extension = os.path.splitext(uploaded_file.name)

    file_key_s3 = compute_file_key_s3(pin.unique_id, uploaded_file_extension)

    try:
        upload_file_to_s3(uploaded_file, file_key_s3)
    except:
        pin.delete()
        response_data = {"errors": [{"code": ERROR_CODE_PIN_CREATION_FAILED}]}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    pin.image_url = compute_file_url_s3(file_key_s3)
    pin.save()

    pin_serializer = PinBasicReadSerializer(pin)

    return Response(pin_serializer.data, status=status.HTTP_201_CREATED)
