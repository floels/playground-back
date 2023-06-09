from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import authentication, signup, accounts, pin_suggestions

schema_view = get_schema_view(
    openapi.Info(
        title="PinIt API",
        default_version="v1",
        license=openapi.License(name="Apache 2.0"),
    ),
    public=True,
)

urlpatterns = [
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger",
    ),
    path("signup/", signup.sign_up, name="sign_up"),
    path(
        "token/obtain/",
        authentication.TokenObtainPairView.as_view(),
        name="obtain_token",
    ),
    path(
        "token/refresh/",
        authentication.TokenRefreshView.as_view(),
        name=("refresh_token"),
    ),
    path("accounts/", accounts.get_accounts, name="get_accounts"),
    path(
        "pin-suggestions/",
        pin_suggestions.GetPinSuggestionsView.as_view(),
        name="get_pin_suggestions",
    ),
]
