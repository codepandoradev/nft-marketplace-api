from app.base.views.base import BaseView
from app.nfts.serializers.nfts.general import POST_NftsSerializer
from app.users.permissions import IsAuthenticatedPermission


class NftsView(BaseView):
    permissions_map = {'post': [IsAuthenticatedPermission]}
    serializer_map = {'post': POST_NftsSerializer}

    def post(self):
        return self.create()

    def get_data(self):
        return self.request.data | {'author': self.request.user}
