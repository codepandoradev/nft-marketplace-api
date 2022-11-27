from app.base.tests.views.base import BaseViewTest
from app.users.models import User
from app.users.tests.factories.users import UserFactory
from app.base.tests.fakers import fake
from app.users.serializers.web3.login import POST_UsersWeb3LoginSerializer


class Web3Test(BaseViewTest):
    path = '/users/web3/login/'

    def test_register_success(self):
        del self.me
        self._test(
            'post',
            [],
            {
                'token': 'lsb16d93kko8zty7o553d7',
                'signature': '0xe960dc37d52a57ef640435f8b33a8b78c5fab13b6e14c40ab0d33d6f7b60bb755ae3a915dd132cdabce6c532398efe79daf9cc48df619e6603e3c8e501b476bd1b',
            },
        )
        print(User.objects.first())

    def test_login_success(self):
        del self.me
        UserFactory(wallet_address='0x0628997825dafda04c2237faa13034c3b878f3fa')
        self._test(
            'post',
            [],
            {
                'token': 'lsb16d93kko8zty7o553d7',
                'signature': '0xe960dc37d52a57ef640435f8b33a8b78c5fab13b6e14c40ab0d33d6f7b60bb755ae3a915dd132cdabce6c532398efe79daf9cc48df619e6603e3c8e501b476bd1b',
            },
        )
        self.assert_equal(User.objects.count(), 1)

    def test_invalid_signature(self):
        del self.me
        UserFactory(wallet_address='0x0628997825dafda04c2237faa13034c3b878f3fa')
        self._test(
            'post',
            POST_UsersWeb3LoginSerializer.WARNINGS[401],
            {
                'token': 'lsb16d93kko8zty7o553d7',
                'signature': fake.english_word(),
            },
        )
