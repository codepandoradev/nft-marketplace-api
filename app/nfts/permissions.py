from app.base.permissions.base import BasePermission
from app.collections.models import Collection
from app.users.models import User


class IsMyCollectionPermission(BasePermission):
    def __init__(self):
        super().__init__()
        self.collection_manager = Collection.objects

    def check(self, user: User, collection: Collection):
        return collection.author == user

    def _has_permission(self, request, view):
        user = request.user
        collection = view.get_valid_serializer().validated_data['collection']
        return self.check(user, collection)
