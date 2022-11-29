import factory

from app.base.tests.factories.base import BaseFactory
from app.base.tests.fakers import Faker
from app.messenger.models import Message
from app.users.tests.factories.users import UserFactory


class MessageFactory(BaseFactory):
    sender = factory.SubFactory(UserFactory)
    receiver = factory.SubFactory(UserFactory)
    text = Faker('english_text')

    class Meta:
        model = Message
