from app.base.filtersets.base import BaseFilterSet
from app.collections.models import Collection


class CollectionsFilterSet(BaseFilterSet):
    class Meta:
        model = Collection
        fields = {'author': ['exact']}
