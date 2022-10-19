from app.base.views.base import BaseView
from app.collections.models import Collection
from app.collections.serializers.detail import GET_CollectionSerializer


class CollectionView(BaseView):
    serializer_map = {'get': GET_CollectionSerializer}
    queryset = Collection.objects.all()

    def get(self):
        return self.retrieve()
