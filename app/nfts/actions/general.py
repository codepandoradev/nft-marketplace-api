from django.core.files import File

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.base.enums.network import Network
from app.nfts.models import Nft
from app.users.models import User


class POST_NftsAction(BaseAction):
    class InEntity(BaseEntity):
        author: User
        network: Network
        content: File
        title: str
        description: str = ''

    def __init__(self):
        self.nft_manager = Nft.objects

    def run(self, data: InEntity) -> Nft:
        return self.nft_manager.create(**data.dict())
