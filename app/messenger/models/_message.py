from django.db import models
from django.utils import timezone

from app.base.models.base import BaseModel
from app.messenger.managers.message import MessageManager
from app.users.models import User


class Message(BaseModel):
    receiver = models.ForeignKey(
        User, models.CASCADE, related_name='messages_by_receiver'
    )
    sender = models.ForeignKey(User, models.CASCADE, related_name='messages_by_sender')
    text = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    objects = MessageManager()

    class Meta:
        ordering = ['-sent_at']


class MessageAttachment(BaseModel):
    message = models.ForeignKey(Message, models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='message_attachment/file')
