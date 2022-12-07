from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from app.base.enums.network import Network
from app.base.serializers.base import BaseModelSerializer
from app.nfts.constans import ALLOWED_NFT_CONTENT_EXTENSIONS
from app.nfts.models import Nft


class POST_NftsSerializer(BaseModelSerializer):
    # price_currency = serializers.ChoiceField(
    #     choices=Currency.choices,
    #     help_text=Currency.help_text,
    #     default=settings.DEFAULT_CURRENCY,
    #     write_only=True,
    # )
    content = serializers.FileField(
        validators=[FileExtensionValidator(ALLOWED_NFT_CONTENT_EXTENSIONS)],
    )

    class Meta:
        model = Nft
        extra_kwargs = {'network': {'help_text': Network.help_text}}
        write_only_fields = [
            'network',
            'content',
            'collection',
            'title',
            'description',
        ]
        read_only_fields = ['slug']
