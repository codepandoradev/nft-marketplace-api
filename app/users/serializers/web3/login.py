from rest_framework import serializers

from app.base.exceptions import APIWarning
from app.base.serializers.base import BaseSerializer


class POST_UsersWeb3LoginSerializer(BaseSerializer):
    WARNINGS = {403: APIWarning("User banned or not active", 403, 'forbidden_login')}

    token = serializers.CharField(write_only=True)
    signature = serializers.CharField(write_only=True)
    auth_token = serializers.CharField(read_only=True)
