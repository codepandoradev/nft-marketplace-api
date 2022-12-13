from app.base.serializers.base import BaseModelSerializer
from app.collections.models import Collection


class GET_CollectionsSerializer(BaseModelSerializer):
    class Meta:
        model = Collection
        read_only_fields = ['slug', 'author', 'avatar', 'title', 'description']


class POST_CollectionsSerializer(BaseModelSerializer):
    class Meta:
        model = Collection
        write_only_fields = ['avatar', 'title', 'description']
        read_only_fields = ['slug']
