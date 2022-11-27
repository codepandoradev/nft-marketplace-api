from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.users.enums.users import UserType
from app.users.models import Token, User
from app.users.serializers.web3.login import POST_UsersWeb3LoginSerializer
from app.users.tests.factories.users import UserFactory


class UsersWeb3LoginTest(BaseViewTest):
    path = '/users/web3/login/'

    me_data = None

    __token = 'lsb16d93kko8zty7o553d7'
    __signature = (
        '0xe960dc37d52a57ef640435f8b33a8b78c5fab13b6e14c40ab0d33d6f7b60bb755ae3a915dd13'
        '2cdabce6c532398efe79daf9cc48df619e6603e3c8e501b476bd1b'
    )
    __wallet_address = '0x0628997825dafda04c2237faa13034c3b878f3fa'

    def test_post_register(self):
        self._test(
            'post',
            {'auth_token': lambda t: self.assert_model(Token, {'key': t})},
            {'token': self.__token, 'signature': self.__signature},
        )
        self.assert_model(User, {'wallet_address': self.__wallet_address})

    def test_post_login(self):
        UserFactory(wallet_address=self.__wallet_address)
        self._test(
            'post',
            {'auth_token': lambda t: self.assert_model(Token, {'key': t})},
            {'token': self.__token, 'signature': self.__signature},
        )
        self.assert_equal(User.objects.count(), 1)

    def test_invalid_signature(self):
        UserFactory(
            wallet_address=self.__wallet_address,
        )
        self._test(
            'post',
            POST_UsersWeb3LoginSerializer.WARNINGS[401],
            {'token': self.__token, 'signature': fake.english_word()},
        )

    def test_user_banned(self):
        UserFactory(wallet_address=self.__wallet_address, type=UserType.BANNED)
        self._test(
            'post',
            POST_UsersWeb3LoginSerializer.WARNINGS[401],
            {'token': self.__token, 'signature': self.__signature},
        )
