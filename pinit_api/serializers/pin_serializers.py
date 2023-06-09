from rest_framework import serializers

from ..models import Account, Pin
from .account_serializers import AccountBaseSerializer


class AccountReadSerializer(AccountBaseSerializer):
    class Meta:
        model = Account
        fields = ("username", "display_name")


class PinWithAuthorReadSerializer(serializers.ModelSerializer):
    author = AccountReadSerializer(read_only=True)

    class Meta:
        model = Pin
        fields = ["id", "image_url", "title", "description", "author"]
