from rest_framework.response import Response

from app.base.exceptions import ClientError
from app.base.views.base import BaseView
from app.nfts.actions.general import POST_NftsAction
from app.nfts.serializers.general import POST_NftsSerializer
from app.users.permissions import AuthenticatedPermission


class NftsView(BaseView):
    permissions_map = {'post': [AuthenticatedPermission]}
    serializer_map = {'post': POST_NftsSerializer}

    def post(self, request):
        action = POST_NftsAction()
        serializer = self.get_valid_serializer()
        try:
            serializer.instance = action.run(
                action.InEntity(creator=self.request.user, **serializer.validated_data)
            )
        except PermissionError:
            raise ClientError(status=403)
        return Response(serializer.data, status=201)
