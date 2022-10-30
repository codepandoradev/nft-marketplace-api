from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as _UserManager

from app.users.enums.users import UserType


class UserManager(_UserManager):
    def create_user(self, wallet_address, password='', **extra_fields):
        user = self.model(wallet_address=wallet_address, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, wallet_address, password='', **extra_fields):
        extra_fields['type'] = UserType.SUPER
        return self.create_user(wallet_address, password, **extra_fields)
