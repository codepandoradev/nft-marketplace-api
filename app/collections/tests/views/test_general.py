from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest
from app.collections.tests.factories.collection import CollectionFactory


class CollectionsTest(BaseViewTest):
    path = '/collections/'

    def test_get(self):
        CollectionFactory()
        CollectionFactory(author=self.me)
        self._test('get', {'count': 2})

    def test_get_my(self):
        CollectionFactory()
        CollectionFactory(author=self.me)
        self._test('get', {'count': 1}, path=f"{self.path}?author={self.me.id}")

    def test_post(self):
        self._test(
            'post',
            {'slug': lambda s: isinstance(s, str)},
            {
                'avatar': fake.image(),
                'title': fake.english_word(),
                'description': fake.english_text(),
            },
            format='multipart',
        )
