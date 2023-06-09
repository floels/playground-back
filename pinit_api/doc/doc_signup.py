from drf_yasg import openapi

SUCCESSFUL_RESPONSE_SCHEMA = openapi.Response(
    description="Successful signup",
    schema=openapi.Schema(
        type="object",
        properties={
            "access_token": openapi.Schema(
                type="string", description="Access token", min_length=1
            ),
            "refresh_token": openapi.Schema(
                type="string", description="Refresh token", min_length=1
            ),
        },
    ),
    examples={
        "application/json": {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4OTk0NTAwLCJpYXQiOjE2Nzg5OT",
            "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTA4MDYwMCwiaWF0IjoxNjc4OTk0MjAwLCJqdGkiOiJlYTcyNTFjNzRmODU0YWFhYmFkNTI5MDBmMTBhOTQ2YiIsInVzZXJfaWQiOjF9.UgC1da2o4bt_K3tqEIQrRwkRx6au1TCK8ftosYJB_cw",
        }
    },
)

BAD_REQUEST_RESPONSE_SCHEMA = openapi.Response(
    description="Invalid signup data",
    schema=openapi.Schema(
        type="object",
        properties={
            "errors": openapi.Schema(
                type="array",
                items=openapi.Schema(
                    type="object",
                    properties={
                        "code": openapi.Schema(
                            type="string",
                            description="Error code",
                            min_length=1,
                            enum=[
                                "invalid_email",
                                "invalid_password",
                                "invalid_birthdate",
                                "email_already_signed_up",
                            ],
                        )
                    },
                ),
            )
        },
    ),
    examples={"application/json": {"errors": [{"code": "email_already_signed_up"}]}},
)

SWAGGER_SCHEMAS = {
    "POST /signup/": {
        "operation_summary": "Sign up",
        "operation_description": "Takes sign-up data, creates a new user and corresponding personal account, and returns a pair of access and refresh token if sign-up was successful.",
        "tags": ["Sign-up and authentication"],
        "security": [],
        "request_body": openapi.Schema(
            type="object",
            properties={
                "email": openapi.Schema(type="string", format="email"),
                "password": openapi.Schema(type="string", format="password"),
                "birthdate": openapi.Schema(type="string", format="date"),
            },
            required=["email", "password", "birthdate"],
            example={
                "email": "john.doe@example.com",
                "password": "J0hnDO€sPA$$W0RD",
                "birthdate": "1970-01-01",
            },
        ),
        "responses": {
            200: SUCCESSFUL_RESPONSE_SCHEMA,
            400: BAD_REQUEST_RESPONSE_SCHEMA,
        },
    },
}
