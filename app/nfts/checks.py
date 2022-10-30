from app.base.checkers.base import BaseChecker
from app.base.entities.base import BaseEntity
from app.collections.models import Collection
from app.users.models import User


class IsMyCollectionChecker(BaseChecker):
    class InEntity(BaseEntity):
        user: User
        collection: Collection

    def __init__(self):
        self.collection_manager = Collection.objects

    def check(self, data: InEntity):
        return data.collection.author == data.user
