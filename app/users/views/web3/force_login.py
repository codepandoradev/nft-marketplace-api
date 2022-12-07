from django.core.validators import RegexValidator
from rest_framework.fields import CharField
from rest_framework.response import Response

from app.base.serializers.base import BaseSerializer
from app.base.views.base import BaseView
from app.users.models import User
from app.users.services.auth import AuthService


class UsersWeb3ForceLoginSerializer(BaseSerializer):
    wallet_address = CharField(
        write_only=True, validators=[RegexValidator(r"^0x[a-z0-9]{40}$")]
    )
    token = CharField(read_only=True)


class UsersWeb3ForceLoginView(BaseView):
    serializer_map = {'post': UsersWeb3ForceLoginSerializer}

    def post(self):
        auth_service = AuthService()
        wallet_address = self.get_valid_serializer().validated_data['wallet_address']
        user = User.objects.get_or_create(wallet_address=wallet_address)[0]
        token = auth_service.login(user, self.request).key
        return Response({'token': token})
