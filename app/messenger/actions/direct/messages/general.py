from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.messenger.models import Message
from app.users.models import User


class POST_MessengerDirectMessagesAction(BaseAction):
    class InEntity(BaseEntity):
        sender: User
        receiver: User
        text: str

    OutEntity = Message

    def __init__(self):
        self.message_manager = Message.objects

    def run(self, data: InEntity) -> OutEntity:
        return self.message_manager.create(**data.dict())
