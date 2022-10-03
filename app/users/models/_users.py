from django.contrib.auth import password_validation
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from app.base.models.base import BaseModel
from app.users.managers import UserManager
from app.users.enums.users import UserType

__all__ = ['User']


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    type = models.PositiveSmallIntegerField(
        choices=UserType.choices, default=UserType.DEFAULT
    )
    wallet_address = models.TextField(unique=True, null=False, default=None)
    password = models.CharField(_('password'), max_length=128, blank=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'wallet_address'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        BaseModel.save(self, *args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
