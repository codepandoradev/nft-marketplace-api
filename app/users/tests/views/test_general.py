from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.users.serializers.token import POST_UsersTokenSerializer
from app.base.tests.views.base import BaseViewTest
from app.users.enums.users import UserType
from app.users.models import User, Token
from app.users.tests.factories.users import UserFactory


class UsersTest(BaseViewTest):
    path = '/users/token/'

    def test_post_success(self):
        user = self.me
        self.client.logout()
        self._test(
            'post',
            {},
            {
                'username': user.username,
                'password': user.raw_password,
            },
        )

    def test_user_not_exist(self):
        self._test(
            'post',
            POST_UsersTokenSerializer.WARNINGS[401],
            {
                'username': fake.english_word(),
                'password': fake.english_word(),
            },
        )

    def test_user_banned(self):
        del self.me
        user = UserFactory(type=UserType.BANNED)
        self._test(
            'post',
            POST_UsersTokenSerializer.WARNINGS[401],
            {
                'username': user.username,
                'password': user.raw_password,
            },
        )

    def test_delete_user(self):
        self.me
        self._test(
            'delete',
            {},
            {},
        )
        self.assert_equal(Token.objects.count(), 0)
