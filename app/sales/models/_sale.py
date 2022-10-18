from django.db import models
from djmoney.models.fields import MoneyField

from app.base.models.base import BaseModel
from app.base.money import Money
from app.nfts.models import Nft
from app.sales.enums import SalePolicy


class Sale(BaseModel):
    nft = models.ForeignKey(Nft, models.CASCADE)
    policy = models.TextField(choices=SalePolicy.choices)
    price: Money = MoneyField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.DurationField()
