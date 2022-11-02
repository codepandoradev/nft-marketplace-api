from app.base.tests.views.base import BaseViewTest


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
