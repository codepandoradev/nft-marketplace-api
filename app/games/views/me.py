from app.base.views.base import BaseView
from app.users.permissions import AuthenticatedPermission
from app.games.serializers.general import (
    GET_UserPointsSerializer,
)


class MeUserPointsView(BaseView):
    permissions_map = {
        'get': [AuthenticatedPermission],
    }
    serializer_map = {'get': GET_UserPointsSerializer}

    def get(self):
        return self.retrieve()

    def get_object(self):
        return self.request.user
