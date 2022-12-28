from django.db.models import Q
from django_filters import filters

from app.base.filtersets.base import BaseFilterSet
from app.users.models import User


class UsersFilterset(BaseFilterSet):
    has_chat = filters.BooleanFilter(
        method='filter_has_chat', label='User has chat with me'
    )

    class Meta:
        model = User
        fields = {'username': ['exact']}
        filter_overrides = {'has_chat': []}

    def filter_has_chat(self, queryset, _, value=False):
        user = self.request.user
        q = Q(messages_by_receiver__sender=user) | Q(messages_by_sender__receiver=user)
        return queryset.filter(q if value else ~q)
