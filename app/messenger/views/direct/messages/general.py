from rest_framework.generics import get_object_or_404

from app.base.paginations.limit_offset import LimitOffsetPagination
from app.base.views.base import BaseView
from app.messenger.models import Message
from app.messenger.serializers.direct.messages.general import (
    GET_MessengerDirectMessagesSerializer,
)
from app.users.models import User
from app.users.permissions import AuthenticatedPermission


class MessengerDirectMessagesView(BaseView):
    many = True
    serializer_map = {'get': GET_MessengerDirectMessagesSerializer}
    permissions_map = {'get': [AuthenticatedPermission]}
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        interlocutor = get_object_or_404(User, pk=self.kwargs['interlocutor'])
        return Message.objects.all_from_direct(interlocutor, self.request.user)

    def get(self):
        return self.list()
