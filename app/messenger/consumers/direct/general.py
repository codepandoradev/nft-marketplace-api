from channels.db import database_sync_to_async
from channels_redis.core import RedisChannelLayer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer

from app.base.consumers import AsyncJsonConsumerMixin
from app.base.exceptions import ClientError
from app.base.exceptions.handler import exception_handler
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

    @property
    def chat_name(self) -> str:
        return f"chat_{'-'.join([str(u.pk) for u in self.users])}"

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
