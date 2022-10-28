from app.base.enums.network import Network
from app.base.exceptions import ClientError
from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.collections.tests.factories.collection import CollectionFactory


class NftsTest(BaseViewTest):
    path = '/nfts/'

    def test_post_error_403(self):
        collection = CollectionFactory()
        self._test(
            'post',
            ClientError(status=403),
            {
                'content': fake.image(extension='gif'),
                'collection': collection.slug,
                'network': fake.random_element(Network),
                'title': fake.random_object_name(),
                'description': fake.english_word(),
            },
            format='multipart',
        )

    def test_post_successful(self):
        user = self.me
        collection = CollectionFactory(author=user)
        self._test(
            'post',
            [],
             {
                'creator': collection.author,
                'network': fake.random_element(Network),
                'collection': collection.slug,
                'content': fake.image(extension='gif'),
                'title': fake.random_object_name(),
                'description': fake.english_word(),
            },
            status=201,
            format='multipart',
        )