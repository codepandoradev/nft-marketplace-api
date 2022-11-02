from app.base.enums.network import Network
from app.base.exceptions import ClientError, APIWarning
from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.collections.tests.factories.collection import CollectionFactory
from app.users.enums.users import UserType


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
                'password':user.password,

            },
            format='multipart',
        )
