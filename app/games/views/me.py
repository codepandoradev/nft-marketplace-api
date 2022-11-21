from app.base.views.base import BaseView
from app.games.serializers.general import GET_GamesSerializer
from app.users.permissions import AuthenticatedPermission


class GamesMeView(BaseView):
    permissions_map = {'get': [AuthenticatedPermission]}
    serializer_map = {'get': GET_GamesSerializer}

    def get(self):
        return self.retrieve()

    def get_object(self):
        return self.request.user
