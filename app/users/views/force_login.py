from django.conf import settings
from rest_framework.fields import CharField
from rest_framework.response import Response

from app.base.exceptions import CriticalError
from app.base.utils.schema import schema_serializer
from app.base.views.base import BaseView
from app.users.models import User
from app.users.services.auth import AuthService


class UsersForceLoginView(BaseView):
    serializer_class = schema_serializer('ForceLogin', token=CharField())

    def get(self):
        if not settings.DEBUG:
            raise CriticalError("force_login is unavailable when not DEBUG")
        auth_service = AuthService()
        user = User.objects.get(id=1)
        token = auth_service.login(user, self.request).key
        return Response({'token': token})
