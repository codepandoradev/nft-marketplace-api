from app.base.serializers.base import BaseModelSerializer
from app.messenger.models import Message


class MessageSerializer(BaseModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ['id', 'receiver', 'sender', 'text']
