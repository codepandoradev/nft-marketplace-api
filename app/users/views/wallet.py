from rest_framework.fields import CharField
from rest_framework.response import Response

from app.base.utils.schema import extend_schema, schema_serializer
from app.base.views.base import BaseView
from app.users.serializers.wallet import *
from app.users.actions.wallet import *


class UsersWalletView(BaseView):
    serializer_map = {'post': POST_UsersWalletSerializer}

    @extend_schema(
        responses={
            201: schema_serializer('POST_UsersWallet', token=CharField(read_only=True))
        }
    )
    def post(self):
        action = POST_UsersWalletAction()
        serializer = self.get_valid_serializer()
        try:
            serializer.instance = action.run(
                action.InEntity(**serializer.validated_data, request=self.request)
            ).dict()
        except PermissionError:
            raise serializer.WARNINGS[401]
        return Response(serializer.data, status=201)
