from rest_framework.response import Response

from app.base.views.base import BaseView
from app.nfts.actions.general import POST_NftsAction
from app.nfts.permissions import IsMyCollectionPermission
from app.nfts.serializers.general import POST_NftsSerializer


class NftsView(BaseView):
    permissions_map = {'post': [IsMyCollectionPermission]}
    serializer_map = {'post': POST_NftsSerializer}

    def post(self, request):
        action = POST_NftsAction()
        serializer = self.get_valid_serializer()
        serializer.instance = action.run(
            action.InEntity(creator=self.request.user, **serializer.validated_data)
        )
        return Response(serializer.data, status=201)
