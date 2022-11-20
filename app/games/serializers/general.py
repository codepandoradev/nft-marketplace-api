from app.base.serializers.base import BaseModelSerializer
from app.users.models import User


class GET_UserPointsSerializer(BaseModelSerializer):
    class Meta:
        model = User
        read_only_fields = [
            'avatar',
            'username',
            'first_score',
            'second_score',
            'third_score',
        ]
