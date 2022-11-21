from app.base.serializers.base import BaseModelSerializer
from app.messenger.models import Message


class GET_MessengerDirectMessagesSerializer(BaseModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ['id', 'receiver', 'sender', 'text', 'sent_at']


class POST_MessengerDirectMessagesSerializer(BaseModelSerializer):
    class Meta:
        model = Message
        write_only_fields = ['text']
        read_only_fields = ['id']
