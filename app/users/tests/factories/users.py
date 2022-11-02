import factory
from django.contrib.auth.hashers import make_password

from app.base.tests.fakers import Faker, fake
from app.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    raw_password: str

    wallet_address = factory.LazyFunction(fake.random_string)
    username = Faker('first_name')
    password = Faker('password')
    avatar = factory.django.ImageField()
    header = factory.django.ImageField()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        raw_password = kwargs['password']
        obj = super(UserFactory, cls)._create(
            model_class, *args, **kwargs | {'password': make_password(raw_password)}
        )
        obj.raw_password = raw_password
        return obj
