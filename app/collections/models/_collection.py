from django.core.validators import RegexValidator
from django.db import models
from uuslug import uuslug

from app.base.models.base import BaseModel
from app.collections.constans import COLLECTION_TITLE_REGEX, COLLECTION_TITLE_MAX_LENGTH
from app.users.models import User


class Collection(BaseModel):
    slug = models.SlugField(primary_key=True)
    author = models.ForeignKey(User, models.CASCADE)
    avatar = models.ImageField(upload_to='collection/avatar')
    title = models.CharField(
        max_length=COLLECTION_TITLE_MAX_LENGTH,
        validators=[RegexValidator(COLLECTION_TITLE_REGEX)],
    )
    description = models.TextField(blank=True, default='')

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, self)
        super().save(*args, **kwargs)
