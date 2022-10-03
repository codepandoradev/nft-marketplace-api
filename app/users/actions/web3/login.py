from rest_framework.request import Request

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.users.models import User
from app.users.services.auth import AuthService
from app.users.utils import recover_to_addr


class POST_UsersWeb3LoginAction(BaseAction):
    class InEntity(BaseEntity):
        token: str
        signature: str
        request: Request

    class OutEntity(BaseEntity):
        auth_token: str

    def __init__(self):
        self.auth_service = AuthService()
        self.user_manager = User.objects

    def run(self, data: InEntity):
        """
        :raises PermissionError: if not auth_service.check_user
        """
        address = recover_to_addr(data.token, data.signature)
        try:
            user = self.user_manager.get(wallet_address=address)
        except User.DoesNotExist:
            user = self.user_manager.create(wallet_address=address, is_active=True)
        return self.OutEntity(
            auth_token=self.auth_service.login(user, data.request).key
        )
