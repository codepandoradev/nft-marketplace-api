from rest_framework.filters import OrderingFilter

from app.base.views.base import BaseView
from app.games.serializers.general import GET_GamesSerializer
from app.users.models import User


class GamesView(BaseView):
    many = True
    serializer_map = {'get': GET_GamesSerializer}
    filter_backends = [OrderingFilter]
    ordering_fields = ['first_score', 'second_score', 'third_score']
    queryset = User.objects.all()

    def get(self):
        return self.list()
