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
                'title': fake.random_object_name(),
                'description': fake.english_text(1000),
            },
            format='multipart',
        )
