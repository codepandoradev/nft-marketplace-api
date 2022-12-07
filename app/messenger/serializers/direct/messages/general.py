from rest_framework import serializers

from app.base.serializers.base import BaseModelSerializer
from app.messenger.models import Message, MessageAttachment


class _GET_MessengerDirectMessages_AttachmentsSerializer(BaseModelSerializer):
    class Meta:
        model = MessageAttachment
        read_only_fields = ['file']


class GET_MessengerDirectMessagesSerializer(BaseModelSerializer):
    attachments = _GET_MessengerDirectMessages_AttachmentsSerializer(many=True)

    class Meta:
        model = Message
        read_only_fields = [
            'id',
            'receiver',
            'sender',
            'text',
            'sent_at',
            'attachments',
        ]


class POST_MessengerDirectMessagesSerializer(BaseModelSerializer):
    attachments = serializers.ListField(default=['<file>'])

    class Meta:
        model = Message
        write_only_fields = ['text', 'attachments']
        read_only_fields = ['id']
