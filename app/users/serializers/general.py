from app.base.serializers.base import BaseModelSerializer
from app.users.models import User


class GET_UsersSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'wallet_address']
