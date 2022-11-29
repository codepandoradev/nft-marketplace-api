from app.base.tests.views.base import BaseViewTest
from app.messenger.tests.factories import MessageFactory
from app.users.models import User
from app.users.tests.factories.users import UserFactory


class MessengerDirectMessagesTest(BaseViewTest):
    interlocutor: User

    @property
    def path(self):
        return f"/messenger/direct/{self.interlocutor.pk}/messages/"

    def test_get_successful(self):
        self.interlocutor = UserFactory()
        message_from_me = MessageFactory(sender=self.me, receiver=self.interlocutor)
        message_to_me = MessageFactory(sender=self.interlocutor, receiver=self.me)
        self._test(
            'get',
            {
                'count': 2,
                'results': lambda ms: self.assertListEqual(
                    [message_to_me.id, message_from_me.id], [m['id'] for m in ms]
                ),
            },
        )
