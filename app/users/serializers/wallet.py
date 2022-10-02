from rest_framework import serializers

from app.base.exceptions import APIWarning
from app.base.serializers.base import BaseModelSerializer
from app.users.models import User


class POST_UsersWalletSerializer(BaseModelSerializer):
    WARNINGS = {
        401: APIWarning("Invalid token or signature", 401, 'invalid_token_or_signature')
    }

    token = serializers.CharField()
    signature = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['token', 'signature']
        write_only_fields = ['signature']
