from rest_framework import generics
from ..serializers.authentication_serializers import UserSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .signup_doc import SWAGGER_SCHEMAS


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(**SWAGGER_SCHEMAS["SignupView"])
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            refresh_token = RefreshToken.for_user(user)

            return JsonResponse(
                {
                    "access": str(refresh_token.access_token),
                    "refresh": str(refresh_token),
                }
            )

        flattened_errors = []

        for field_errors in serializer.errors.values():
            for error in field_errors:
                flattened_errors.append({"code": str(error)})

        return JsonResponse({"errors": flattened_errors}, status=400)
