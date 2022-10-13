from django.conf import settings
from rest_framework import serializers

from app.base.enums.currency import Currency
from app.base.enums.network import Network
from app.base.serializers.base import BaseModelSerializer
from app.base.serializers.fields.base64_image import Base64ImageField
from app.nfts.models import Nft
from app.sale.enums import SalesPolicy


class POST_NftsSerializer(BaseModelSerializer):
    author = serializers.HiddenField(default=None)
    price_currency = serializers.ChoiceField(
        choices=Currency.choices,
        help_text=Currency.help_text,
        default=settings.DEFAULT_CURRENCY,
        write_only=True,
    )
    content = Base64ImageField(write_only=True)

    class Meta:
        model = Nft
        extra_kwargs = {
            'network': {'help_text': Network.help_text},
            'sales_policy': {'help_text': SalesPolicy.help_text},
        }
        write_only_fields = [
            'author',
            'network',
            'content',
            'sales_policy',
            'price',
            'price_currency',
            'title',
            'description',
        ]
        fields = ['id']
