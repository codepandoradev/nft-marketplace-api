from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from channels_redis.core import RedisChannelLayer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer

from app.base.consumers import AsyncJsonConsumerMixin
from app.base.exceptions import ClientError
from app.base.exceptions.handler import exception_handler
from app.messenger.models import Message
from app.messenger.serializers.direct.messages.general import (
    GET_MessengerDirectMessagesSerializer,
)
from app.users.models import User
from app.users.permissions import AuthenticatedPermission


class MessengerDirectConsumer(AsyncJsonConsumerMixin, GenericAsyncAPIConsumer):
    channel_layer: RedisChannelLayer

    queryset = User.objects.all()
    permission_classes = [AuthenticatedPermission]

    def __init__(self):
        AsyncJsonConsumerMixin.__init__(self)
        GenericAsyncAPIConsumer.__init__(self)
        self.users: set[User] = set()

    @staticmethod
    def get_chat_name(users: set[User]) -> str:
        return f"chat_{'-'.join([str(u.pk) for u in users])}"

    @property
    def chat_name(self) -> str:
        return self.get_chat_name(self.users)

    async def handle_exception(self, exception: Exception, action: str, request_id):
        response = exception_handler(exception)
        await self.reply(
            action=action,
            errors=response.data,
            status=response.status_code,
            request_id=request_id,
        )

    async def websocket_connect(self, message):
        try:
            return await super().websocket_connect(message)
        except Exception as exception:
            exception_handler(exception)
            await self.close()

    async def connect(self):
        try:
            interlocutor = await database_sync_to_async(self.get_object)(
                pk=self.scope['url_route']['kwargs']['interlocutor']
            )
        except KeyError as exc:
            raise ClientError("`interlocutor` query param wasn't given") from exc
        self.users = {self.scope['user'], interlocutor}
        await self.channel_layer.group_add(self.chat_name, self.channel_name)
        await self.accept()

    async def new_message(self, event):
        await self.send_json(event)

    @classmethod
    def send_new_message(cls, message: Message) -> None:
        channel_layer: RedisChannelLayer = get_channel_layer()
        serializer = GET_MessengerDirectMessagesSerializer(instance=message)
        async_to_sync(channel_layer.group_send)(
            cls.get_chat_name({message.sender, message.receiver}),
            {'type': 'new_message', 'message': serializer.data},
        )
