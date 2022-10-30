from app.base.tests.fakers import fake
from app.base.tests.views.base import BaseViewTest


class CollectionsTest(BaseViewTest):
    path = '/collections/'

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
