from rest_framework.response import Response

from app.base.exceptions import ClientError
from app.base.views.base import BaseView
from app.games.actions.add_points import POST_AddPointsAction
from app.games.serializers.add_points import POST_AddPointsSerializer
from app.users.permissions import AuthenticatedPermission


class AddPointsView(BaseView):
    permissions_map = {'post': [AuthenticatedPermission]}
    serializer_map = {'post': POST_AddPointsSerializer}

    def post(self, request):
        action = POST_AddPointsAction()
        serializer = self.get_valid_serializer()
        try:
            serializer.instance = action.run(
                action.InEntity(user=self.request.user, **serializer.validated_data)
            )
        except PermissionError:
            raise ClientError(status=403)
        return Response(serializer.data, status=201)
