import json

from web3 import Web3
from web3.middleware import geth_poa_middleware

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.base.enums.network import Network
from app.nfts.models import Nft


class POST_SendingAction(BaseAction):
    class InEntity(BaseEntity):
        raw_transaction: str
        nft: Nft

    class OutEntity(BaseEntity):
        transaction_id: str

    # TODO засунуть в другое место. Дубликат в .sending.POST_SendingAction
    _providers = {
        Network.BSC: 'https://bsc-dataseed.binance.org/',
        Network.SOL: 'https://api.mainnet-beta.solana.com/',
        Network.POLYGON: 'https://rpc-mainnet.maticvigil.com/',
        Network.ETH: 'https://mainnet.infura.io/v3/',
        Network.TON: 'https://toncenter.com/api/v2/',
    }

    def run(self, data: InEntity) -> OutEntity:
        if data.nft.network != Network.ETH:
            raise NotImplemented
        web3 = Web3(Web3.HTTPProvider(self._providers[data.nft.network]))
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        txn_hash = web3.eth.sendRawTransaction(data.raw_transaction)

        # TODO изменение nft в БД

        return self.OutEntity(transaction_id=txn_hash)
