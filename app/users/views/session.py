from django.contrib.auth import login
from rest_framework.response import Response

from app.base.exceptions import ClientError
from app.base.views.base import BaseView
from app.users.models import User


class UsersSessionView(BaseView):
    def get(self):
        qs = self.request.query_params
        try:
            username, password = qs['username'], qs['password']
        except KeyError as exc:
            raise ClientError("Wasn't provided username and password") from exc
        try:
            user = User.objects.get(username=username)
            if not user.is_staff or not user.check_password(password):
                raise PermissionError
        except (User.DoesNotExist, PermissionError) as exc:
            raise ClientError("Invalid credentials") from exc
        login(self.request, user)
        return Response()
