from django.core.files import File

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.collections.models import Collection
from app.users.models import User


class POST_CollectionsAction(BaseAction):
    class InEntity(BaseEntity):
        author: User
        avatar: File
        title: str
        description: str = ''

    def __init__(self):
        self.collection_manager = Collection.objects

    def run(self, data: InEntity) -> Collection:
        return self.collection_manager.create(**data.dict())
