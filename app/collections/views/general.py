from rest_framework.response import Response

from app.base.views.base import BaseView
from app.collections.actions.general import POST_CollectionsAction
from app.collections.serializers.general import POST_CollectionsSerializer
from app.users.permissions import AuthenticatedPermission


class CollectionsView(BaseView):
    permissions_map = {'post': [AuthenticatedPermission]}
    serializer_map = {'post': POST_CollectionsSerializer}

    def post(self):
        action = POST_CollectionsAction()
        serializer = self.get_valid_serializer()
        serializer.instance = action.run(
            action.InEntity(author=self.request.user, **serializer.validated_data)
        )
        return Response(serializer.data, status=201)
