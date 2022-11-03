from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.users.serializers.token import POST_UsersTokenSerializer


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
            format='multipart',
        )

    def test_user_not_exist(self):
        self._test(
            'post',
            POST_UsersTokenSerializer.WARNINGS[401],
            {
                'username': fake.english_word(),
                'password': fake.english_word(),
            },
            format='multipart',
        )
