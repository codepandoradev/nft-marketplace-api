import json

from web3 import Web3
from web3.middleware import geth_poa_middleware

from app.base.actions.base import BaseAction
from app.base.entities.base import BaseEntity
from app.base.enums.network import Network
from app.nfts.models import Nft
from app.users.models import User


class POST_MintingAction(BaseAction):
    class InEntity(BaseEntity):
        nft: Nft
        owner: User

    class OutEntity(BaseEntity):
        transaction: dict

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

        owner_addr = Web3.toChecksumAddress(data.owner.wallet_address)

        sc_abi = json.loads('')  # TODO метод для минта
        sc_address = Web3.toChecksumAddress('0x7f268357A8c2552623316e2562D90e642bB538E5')  # TODO OpenSea
        smart_contract = web3.eth.contract(sc_address, abi=sc_abi)

        nonce = web3.eth.getTransactionCount(owner_addr)

        dict_transaction = {
            'chainId': web3.eth.chain_id,
            'from': owner_addr,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce,
        }

        # создаём транзакцию
        transaction = smart_contract.functions.transfer(
            
        ).buildTransaction(dict_transaction)

        return self.OutEntity(raw_transaction=transaction)

