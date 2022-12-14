from hashlib import md5

from rest_framework import serializers

from app.base.exceptions import ClientError
from app.base.serializers.base import BaseModelSerializer
from app.users.models import User


class POST_AddPointsSerializer(BaseModelSerializer):
    game_index = serializers.IntegerField(write_only=True, min_value=1, max_value=3)
    score_to_add = serializers.IntegerField(write_only=True, min_value=0)
    secret_key = serializers.CharField(write_only=True)

    def is_valid(self, raise_exception=True):
        super().is_valid()
        server_md5_key = md5(
            (
                md5(
                    ('aboba' + str(self.validated_data['game_index'])).encode('utf-8')
                ).hexdigest()
                + 'ikm6fjlotuy7p88li678'
                + self.context['request'].user.wallet_address
                + str(self.validated_data['score_to_add'])
            ).encode('utf-8')
        ).hexdigest()

        if server_md5_key != self.validated_data['secret_key']:
            raise ClientError('Incorrect secret key.')

    class Meta:
        model = User
        write_only_fields = [
            'game_index',
            'score_to_add',
            'secret_key',
        ]
        read_only_fields = [
            'avatar',
            'username',
            'first_score',
            'second_score',
            'third_score',
            'wallet_address',
        ]
