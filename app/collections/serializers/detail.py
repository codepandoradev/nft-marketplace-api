from app.base.serializers.base import BaseModelSerializer
from app.collections.models import Collection


class GET_CollectionSerializer(BaseModelSerializer):
    class Meta:
        model = Collection
        read_only_fields = ['title', 'avatar', 'description']
