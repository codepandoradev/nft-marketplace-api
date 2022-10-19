import moneyed

from app.base.enums.base import BaseEnumStr


class Currency(BaseEnumStr):
    ETH = 'Ethereum'


for _currency in tuple(Currency):
    moneyed.add_currency(code=_currency, numeric=None, name=_currency.label)
