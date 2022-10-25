from app.base.permissions.base import BasePermission
from app.nfts.checks import IsMyCollectionChecker
from app.users.checkers import AuthenticatedChecker


class IsMyCollectionPermission(BasePermission):
    requires_authentication = True

    def __init__(self):
        self.authenticated_checker = AuthenticatedChecker()
        self.is_my_collection_checker = IsMyCollectionChecker()

    def _has_permission(self, view):
        user = view.request.user
        if not self.authenticated_checker.check(user):
            return False
        collection = view.get_valid_serializer().validated_data['collection']
        return self.is_my_collection_checker.check(
            self.is_my_collection_checker.InEntity(user=user, collection=collection)
        )
