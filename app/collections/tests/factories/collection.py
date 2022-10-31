import factory

from app.base.tests.factories.base import BaseFactory
from app.base.tests.fakers import Faker
from app.collections.models import Collection
from app.users.tests.factories.users import UserFactory


class CollectionFactory(BaseFactory):
    author = factory.SubFactory(UserFactory)
    title = Faker('english_word')
    avatar = factory.django.ImageField()

    class Meta:
        model = Collection
