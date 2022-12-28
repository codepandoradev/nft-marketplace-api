from app.base.views.base import BaseView
from app.users.filtersets.general import UsersFilterset
from app.users.models import User
from app.users.permissions import AuthenticatedPermission
from app.users.serializers.general import GET_UsersSerializer


class UsersView(BaseView):
    many = True
    serializer_map = {'get': GET_UsersSerializer}
    permissions_map = {'get': [AuthenticatedPermission]}
    queryset = User.objects.all()
    filterset_class = UsersFilterset

    def get(self):
        return self.list()
