from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.text import slugify
from djmoney.models.fields import MoneyField

from app.base.enums.network import Network
from app.base.models.base import BaseModel
from app.base.money import Money
from app.nfts.constans import ALLOWED_NFT_CONTENT_EXTENSIONS, NFT_TITLE_REGEX
from app.sale.enums import SalesPolicy
from app.users.models import User

__all__ = ['Nft']


class Nft(BaseModel):
    author = models.ForeignKey(User, models.CASCADE)
    network = models.TextField(choices=Network.choices)
    content = models.ImageField(
        validators=[FileExtensionValidator(ALLOWED_NFT_CONTENT_EXTENSIONS)]
    )
    sales_policy = models.TextField(choices=SalesPolicy.choices)
    price: Money = MoneyField(max_digits=10, decimal_places=2)
    title = models.CharField(
        max_length=30,
        validators=[RegexValidator(NFT_TITLE_REGEX)],
    )
    slug = models.SlugField()
    description = models.TextField(blank=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
