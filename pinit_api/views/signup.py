from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from ..doc.doc_signup import SWAGGER_SCHEMAS
from ..utils import (
    compute_username_candidate_from_email,
    compute_first_and_last_name_from_email,
    compute_initial_from_email,
)
from ..models import Account
from ..serializers import UserCreateSerializer


def compute_default_account_username_from_email(email):
    username_candidate = compute_username_candidate_from_email(email)

    return compute_default_account_username_from_candidate(username_candidate)


def compute_default_account_username_from_candidate(username_candidate):
    if Account.objects.filter(username=username_candidate):
        return compute_first_available_username_from_candidate(username_candidate)

    # No account exists with this candidate
    return username_candidate


def compute_first_available_username_from_candidate(username_candidate):
    accounts_with_username_starting_with_candidate = Account.objects.filter(
        username__startswith=username_candidate
    )

    usernames_starting_with_candidate = [
        account.username for account in accounts_with_username_starting_with_candidate
    ]

    # Starting from 1, we increment a suffix until the resulting username does not already exist:
    suffix = 1

    while True:
        username = f"{username_candidate}{suffix}"

        if username not in usernames_starting_with_candidate:
            break

        suffix += 1

    return username


def create_personal_account_for_user(user):
    email = user.email

    username = compute_default_account_username_from_email(email)
    first_name, last_name = compute_first_and_last_name_from_email(email)
    initial = compute_initial_from_email(email)

    Account.objects.create(
        username=username,
        type="personal",
        first_name=first_name,
        last_name=last_name,
        initial=initial,
        owner=user,
    )


@swagger_auto_schema(method="post", **SWAGGER_SCHEMAS["POST /signup/"])
@api_view(["POST"])
def sign_up(request):
    user_serializer = UserCreateSerializer(data=request.data)

    if user_serializer.is_valid():
        user = user_serializer.save()

        create_personal_account_for_user(user)

        tokens_pair = RefreshToken.for_user(user)

        return JsonResponse(
            {
                "access_token": str(tokens_pair.access_token),
                "refresh_token": str(tokens_pair),
            }
        )

    flattened_errors = []

    for field_errors in user_serializer.errors.values():
        for error in field_errors:
            flattened_errors.append({"code": str(error)})

    return JsonResponse({"errors": flattened_errors}, status=400)
