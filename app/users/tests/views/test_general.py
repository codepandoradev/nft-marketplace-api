from app.base.tests.views.base import BaseViewTest
from app.messenger.tests.factories import MessageFactory
from app.users.tests.factories.users import UserFactory


class UsersTest(BaseViewTest):
    path = '/users/'

    def test_get_filter_username(self):
        user = UserFactory()
        self._test(
            'get',
            {
                'count': 1,
                'results': lambda res: self.assertEqual(res[0]['id'], user.id),
            },
            path=f"{self.path}?username={user.username}",
        )

    def test_get_filter_has_chat_true(self):
        user_with_chat = UserFactory()
        user_without_chat = UserFactory()
        MessageFactory(sender=self.me, receiver=user_with_chat)
        MessageFactory(sender=user_with_chat, receiver=user_without_chat)
        self._test(
            'get',
            {
                'count': 1,
                'results': lambda res: self.assertEqual(
                    res[0]['id'], user_with_chat.id
                ),
            },
            path=f"{self.path}?has_chat=true",
        )
