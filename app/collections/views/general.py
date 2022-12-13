from rest_framework.response import Response

from app.base.views.base import BaseView
from app.collections.actions.general import POST_CollectionsAction
from app.collections.filtersets.general import CollectionsFilterSet
from app.collections.models import Collection
from app.collections.serializers.general import (
    GET_CollectionsSerializer,
    POST_CollectionsSerializer,
)
from app.users.permissions import AuthenticatedPermission


class CollectionsView(BaseView):
    many = True
    permissions_map = {'post': [AuthenticatedPermission]}
    serializer_map = {
        'get': GET_CollectionsSerializer,
        'post': POST_CollectionsSerializer,
    }
    queryset = Collection.objects.all()
    filterset_class = CollectionsFilterSet

    def get(self):
        return self.list()

    def post(self):
        action = POST_CollectionsAction()
        serializer = self.get_valid_serializer()
        serializer.instance = action.run(
            action.InEntity(author=self.request.user, **serializer.validated_data)
        )
        return Response(serializer.data, status=201)
