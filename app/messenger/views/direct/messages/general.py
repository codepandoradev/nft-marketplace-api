from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app.base.paginations.limit_offset import LimitOffsetPagination
from app.base.views.base import BaseView
from app.messenger.actions.direct.messages.general import (
    POST_MessengerDirectMessagesAction,
)
from app.messenger.models import Message
from app.messenger.serializers.direct.messages.general import (
    GET_MessengerDirectMessagesSerializer,
    POST_MessengerDirectMessagesSerializer,
)
from app.users.models import User
from app.users.permissions import AuthenticatedPermission


class MessengerDirectMessagesView(BaseView):
    many = True
    lookup_url_kwarg = 'interlocutor'
    serializer_map = {
        'get': GET_MessengerDirectMessagesSerializer,
        'post': POST_MessengerDirectMessagesSerializer,
    }
    permissions_map = {
        'get': [AuthenticatedPermission],
        'post': [AuthenticatedPermission],
    }
    pagination_class = LimitOffsetPagination

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs[self.lookup_url_kwarg])

    def get_queryset(self):
        return Message.objects.all_from_direct(self.get_object(), self.request.user)

    def get(self):
        return self.list()

    def post(self):
        action = POST_MessengerDirectMessagesAction()
        serializer = self.get_valid_serializer()
        serializer.instance = action.run(
            action.InEntity(
                sender=self.request.user,
                receiver=self.get_object(),
                **serializer.validated_data,
            )
        )
        return Response(serializer.data, status=201)
