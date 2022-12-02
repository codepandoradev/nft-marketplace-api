from app.base.serializers.base import BaseModelSerializer
from app.users.enums.users import UserType
from app.users.models import User


class GET_UsersMeSerializer(BaseModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'type': {'help_text': UserType.help_text}}
        read_only_fields = [
            'id',
            'type',
            'username',
            'wallet_address',
            'first_top',
            'avatar',
            'header',
        ]


class PATCH_UsersMeSerializer(BaseModelSerializer):
    class Meta:
        model = User
        write_only_fields = ['avatar', 'header']
