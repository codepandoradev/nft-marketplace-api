from django.core.validators import FileExtensionValidator
from django.db import models

from app.base.enums.network import Network
from app.base.models.base import BaseModel
from app.nft.constans import ALLOWED_NFT_CONTENT_EXTENSIONS
from app.sale.enums import SalesPolicy

__all__ = ['Nft']


class Nft(BaseModel):
    author = models.ForeignKey('app.User', models.CASCADE)
    network = models.CharField(choices=Network.choices)
    content = models.ImageField(
        validators=[FileExtensionValidator(ALLOWED_NFT_CONTENT_EXTENSIONS)]
    )
    sales_policy = models.CharField(choices=SalesPolicy.choices)
    # price = MoneyField()
