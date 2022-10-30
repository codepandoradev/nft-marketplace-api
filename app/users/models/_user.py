from django.contrib.auth import password_validation
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from app.base.models.base import BaseModel
from app.users.managers import UserManager
from app.users.enums.users import UserType

__all__ = ['User']


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    type = models.PositiveSmallIntegerField(
        choices=UserType.choices, default=UserType.DEFAULT
    )
    wallet_address = models.TextField(unique=True)
    username = models.CharField(
        max_length=150, unique=True, null=True, blank=True, default=None
    )
    password = models.CharField(max_length=128, blank=True, default='')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['wallet_address']

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        BaseModel.save(self, *args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
