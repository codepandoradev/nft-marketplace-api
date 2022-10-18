from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from uuslug import uuslug

from app.base.enums.network import Network
from app.base.models.base import BaseModel
from app.collections.models import Collection
from app.nfts.constans import ALLOWED_NFT_CONTENT_EXTENSIONS, NFT_TITLE_REGEX
from app.users.models import User

__all__ = ['Nft']


class Nft(BaseModel):
    creator = models.ForeignKey(User, models.CASCADE, related_name='nfts_by_creator')
    owner = models.ForeignKey(User, models.CASCADE, related_name='nfts_by_owner')
    collection = models.ForeignKey(Collection, models.CASCADE)
    network = models.TextField(choices=Network.choices)
    content = models.FileField(
        upload_to='nft/content',
        validators=[FileExtensionValidator(ALLOWED_NFT_CONTENT_EXTENSIONS)],
    )
    title = models.CharField(
        max_length=30,
        validators=[RegexValidator(NFT_TITLE_REGEX)],
    )
    slug = models.SlugField()
    description = models.TextField(blank=True, default='')

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, self)
        super().save(*args, **kwargs)
