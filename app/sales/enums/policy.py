from app.base.enums.base import BaseEnumStr


class SalePolicy(BaseEnumStr):
    FIXED = 'Fixed price'
    BET = 'Open for betting'
    AUCTION = 'Temporary auction'
