from django.db import models

from app.base.models.base import BaseModel
from app.collections.models import Collection


class Exhibition(BaseModel):
    collection = models.OneToOneField(Collection, models.CASCADE)
    start_at = models.DateTimeField()
