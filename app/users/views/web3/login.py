from rest_framework.response import Response

from app.base.views.base import BaseView
from app.users.serializers.web3.login import *
from app.users.actions.web3.login import *


class UsersWeb3LoginView(BaseView):
    serializer_map = {'post': POST_UsersWeb3LoginSerializer}

    def post(self):
        action = POST_UsersWeb3LoginAction()
        serializer = self.get_valid_serializer()
        try:
            serializer.instance = action.run(
                action.InEntity(**serializer.validated_data, request=self.request)
            ).dict()
        except PermissionError:
            raise serializer.WARNINGS[401]
        return Response(serializer.data, status=201)
