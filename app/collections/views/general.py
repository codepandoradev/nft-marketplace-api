from rest_framework.response import Response

from app.base.views.base import BaseView
from app.collections.actions.general import POST_CollectionsAction
from app.collections.serializers.general import POST_CollectionsSerializer
from app.users.permissions import IsAuthenticatedPermission


class CollectionsView(BaseView):
    permissions_map = {'post': [IsAuthenticatedPermission]}
    serializer_map = {'post': POST_CollectionsSerializer}

    def post(self):
        action = POST_CollectionsAction()
        serializer = self.get_valid_serializer()
        serializer.instance = action.run(
            action.InEntity(**serializer.validated_data | {'author': self.request.user})
        )
        return Response(serializer.data, status=201)
