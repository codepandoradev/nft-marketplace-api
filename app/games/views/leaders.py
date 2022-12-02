from app.users.models import User
from rest_framework.response import Response
from app.base.views.base import BaseView


class LeadersView(BaseView):
    queryset = User.objects.all()

    def get(self, request):
        resp_data = [
            {
                'wallet_address': '0x41dfc62c8ce48ca8440f11a979186e947b40b8b8',
                'points': 19560,
            },
            {
                'wallet_address': '0xdb442f218342af64dca5bd97d3564d37e9ccf127',
                'points': 16560,
            },
            {
                'wallet_address': '0x24e9722cd7cb4d398ee115eb575a0093665f8242',
                'points': 13560,
            },
            {
                'wallet_address': '0x078dfc7ffa8ddfa923a448b062ae7f9b2b3f672f',
                'points': 9980,
            },
            {
                'wallet_address': '0x116e24a95be9d32c8df55137a17f190e92342197',
                'points': 8390,
            },
            {
                'wallet_address': '0xe98a5c2cfdc8c3cf1c4a93e6c68ff149e9aab09f',
                'points': 6150,
            },
            {
                'wallet_address': '0xc523fdea9228d7786bd97298ddb545ed00d3c11f',
                'points': 5130,
            },
            {
                'wallet_address': '0x6191b0f82d771b33f9512b73dacc2a05f703ae8c',
                'points': 4780,
            },
            {
                'wallet_address': '0xb3843490720a5a4503b09ffb31a8a40d46274759',
                'points': 4570,
            },
            {
                'wallet_address': '0x6857b246a90c44803ba99269548bb51490731924',
                'points': 4090,
            },
            {
                'wallet_address': '0xde2238f57830916f1cd112322014e017ea348028',
                'points': 3000,
            },
            {
                'wallet_address': '0xf2f5c73fa04406b1995e397b55c24ab1f3ea726c',
                'points': 2970,
            },
            {
                'wallet_address': '0xdf63944d806e838f0cc52e3d7afd11c02fe0cfa5',
                'points': 2780,
            },
            {
                'wallet_address': '0xd73d368ee5f60840a3417f65acc0b1cbeebf5c5b',
                'points': 2170,
            },
            {
                'wallet_address': '0x8ea6e5650990efe2b2fafb132bf52e46104b936c',
                'points': 280,
            },
            {
                'wallet_address': '0xf2691a7fa207113a9cc6d5a10abb9dbcc9516047',
                'points': 0,
            },
            {
                'wallet_address': '0xd29d2b7257c1aec545734015160da63376e0b0e5',
                'points': 0,
            },
            {
                'wallet_address': '0xf9346fb218e90649155a6f90b050c54e5877fa2e',
                'points': 0,
            },
            {
                'wallet_address': '0x6faacf35aebb6b71bc9d1b6a669ec6be22e95df3',
                'points': 0,
            },
            {
                'wallet_address': '0x58df87798fd7f93f30fdfbd1a8aa370f10e49fd1',
                'points': 0,
            },
            {
                'wallet_address': '0xb616858a890dc2062c276899511cab1074b1f584',
                'points': 0,
            },
            {
                'wallet_address': '0x2eb085b6302169ca1f3a27b40a6a70da1404817f',
                'points': 0,
            },
            {
                'wallet_address': '0x232f53dbf4efa2d8ad5606a29a30027fb2b17c5e',
                'points': 0,
            },
            {
                'wallet_address': '0x40d3937720a0072aa93f07e772d2bc3c9c498976',
                'points': 0,
            },
            {
                'wallet_address': '0xe1d5bd00d59625379e3c3e0093c108de795f4387',
                'points': 0,
            },
            {
                'wallet_address': '0x0628997825dafda04c2237faa13034c3b878f3fa',
                'points': 0,
            },
            {
                'wallet_address': '0x6be27924a6dd786f7c1d5737b0995fc8077c39e8',
                'points': 0,
            },
            {
                'wallet_address': '0x2cd183f11df06324da621b714b1e75973b9775c8',
                'points': 0,
            },
            {
                'wallet_address': '0x80567a80861f08f74b4bb1f95f4f78b07e5ca37a',
                'points': 0,
            },
            {
                'wallet_address': '0x4e61e190bc3a823800b5443bc8011ab84f30560c',
                'points': 0,
            },
        ]
        return Response(resp_data, status=201)
