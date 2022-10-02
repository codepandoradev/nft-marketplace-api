from django.conf import settings
from rest_framework.request import Request

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.users.enums.users import UserType
from app.users.models import User
from app.users.services.auth import AuthService
from app.users.utils import recover_to_addr


class POST_UsersWalletAction(BaseAction):
    class InEntity(BaseEntity):
        token: str
        signature: str
        request: Request

    class OutEntity(BaseEntity):
        token: str

    def __init__(self):
        self.auth_service = AuthService()

    def run(self, data: InEntity):
        addr = recover_to_addr(data.token, data.signature)
        try:
            kwarg = {settings.WEB3AUTH_USER_WALLET_ADDRESS_FIELD: addr}
            user = User.objects.get(**kwarg)
        except User.DoesNotExist:
            user = User.objects.create(wallet_address=addr)
        if user.type == UserType.BANNED:
            raise PermissionError
        if not user.is_active:
            raise PermissionError
        return self.OutEntity(token=self.auth_service.login(user, data.request).key)
