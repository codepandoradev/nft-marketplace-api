from app.base.utils.common import response_204
from app.base.views.base import BaseView
from app.users.permissions import AuthenticatedPermission
from app.users.serializers.me.general import (
    GET_UsersMeSerializer,
    PATCH_UsersMeSerializer,
)


class UsersMeView(BaseView):
    permissions_map = {
        'get': [AuthenticatedPermission],
        'patch': [AuthenticatedPermission],
    }
    serializer_map = {'get': GET_UsersMeSerializer, 'patch': PATCH_UsersMeSerializer}

    def get(self):
        return self.retrieve()

    @response_204
    def patch(self):
        self.update()

    def get_object(self):
        return self.request.user
