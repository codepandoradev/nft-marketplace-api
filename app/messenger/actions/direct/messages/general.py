from django.core.files import File

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.messenger.consumers import MessengerDirectConsumer
from app.messenger.models import Message, MessageAttachment
from app.users.models import User


class POST_MessengerDirectMessagesAction(BaseAction):
    class InEntity(BaseEntity):
        sender: User
        receiver: User
        text: str
        attachments: list[File] = []

    OutEntity = Message

    def __init__(self):
        self.message_manager = Message.objects
        self.message_attachment_manager = MessageAttachment.objects

    def run(self, data: InEntity) -> OutEntity:
        message = self.message_manager.create(**data.dict(exclude={'attachments'}))
        for attachment in data.attachments:
            self.message_attachment_manager.create(message=message, file=attachment)
        MessengerDirectConsumer.send_new_message(message)
        return message
