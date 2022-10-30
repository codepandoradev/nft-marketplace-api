from rest_framework import serializers

from app.base.exceptions import APIWarning
from app.base.serializers.base import BaseSerializer


class POST_UsersWeb3LoginSerializer(BaseSerializer):
    WARNINGS = {401: APIWarning("Invalid credentials", 401, 'invalid_credentials')}

    token = serializers.CharField(write_only=True)
    signature = serializers.CharField(write_only=True)
    auth_token = serializers.CharField(read_only=True)
