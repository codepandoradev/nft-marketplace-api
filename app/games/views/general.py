from rest_framework.filters import OrderingFilter

from app.base.views.base import BaseView
from app.games.serializers.general import (
    GET_UserPointsSerializer,
)
from app.users.models import User


class UsersPointsView(BaseView):
    serializer_map = {'get': GET_UserPointsSerializer}
    filter_backends = [OrderingFilter]
    ordering_fields = ['first_score', 'second_score', 'third_score']

    def get(self, request):
        return self.list()

    def get_queryset(self):
        return User.objects.all()
