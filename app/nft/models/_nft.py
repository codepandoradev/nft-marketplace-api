from django.core.validators import FileExtensionValidator
from django.db import models
from djmoney.models.fields import MoneyField

from app.base.enums.network import Network
from app.base.models.base import BaseModel
from app.base.money import Money
from app.nft.constans import ALLOWED_NFT_CONTENT_EXTENSIONS
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
    # FIXME:
    #  https://github.com/codepandoradev/nft-marketplace-api/issues/5#issuecomment
    #  -1276668268
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
