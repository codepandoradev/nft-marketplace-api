from rest_framework.response import Response

from app.base.views.base import BaseView
from app.nfts.actions.general import POST_NftsAction
from app.nfts.serializers.general import POST_NftsSerializer
from app.users.permissions import IsAuthenticatedPermission


class NftsView(BaseView):
    permissions_map = {'post': [IsAuthenticatedPermission]}
    serializer_map = {'post': POST_NftsSerializer}

    def post(self, request):
        action = POST_NftsAction()
        serializer = self.get_valid_serializer(data=self.get_data())
        serializer.instance = action.run(
            action.InEntity(author=self.request.user, **serializer.validated_data)
        )
        return Response(serializer.data, status=201)
