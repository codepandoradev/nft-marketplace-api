from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.messenger.models import Message, MessageAttachment
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

    def test_post_message_success(self):
        self.interlocutor = UserFactory()
        self._test(
            'post',
            data={'text': fake.english_text()},
        )
        self.assert_equal(Message.objects.count(), 1)

    def test_post_message_pick_success(self):
        self.interlocutor = UserFactory()
        self._test(
            'post',
            {},
            {'text': fake.english_text(), 'attachments': fake.image()},
            format='multipart',
        )
        self.assert_equal(Message.objects.count(), 1)
        self.assert_equal(MessageAttachment.objects.count(), 1)
