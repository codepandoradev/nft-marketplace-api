from django.db.models import Manager, Q, QuerySet

from app.users.models import User


class MessageManager(Manager):
    def all_from_direct(self, user_1: User, user_2: User, /) -> QuerySet:
        return self.filter(
            Q(receiver=user_1) & Q(sender=user_2)
            | Q(receiver=user_2) & Q(sender=user_1)
        )
