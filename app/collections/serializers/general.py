from app.base.serializers.base import BaseModelSerializer
from app.collections.models import Collection


class POST_CollectionsSerializer(BaseModelSerializer):
    class Meta:
        model = Collection
        write_only_fields = ['avatar', 'title', 'description']
        read_only_fields = ['slug']
