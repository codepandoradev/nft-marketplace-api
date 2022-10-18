import datetime
from typing import Callable, Final, Optional, Union, Sequence, Dict, List, Any

from django.core.files.base import ContentFile
from factory import Faker as _FactoryFaker
from faker import Faker as _Faker, Generator


class SubFaker(_Faker):
    first_name: Callable[..., str]
    last_name: Callable[..., str]
    password: Callable[..., str]
    email: Callable[..., str]
    future_date: Callable[..., datetime.date]

    def __init__(
        self,
        locale: Optional[
            Union[str, Sequence[str], Dict[str, Union[int, float]]]
        ] = 'en_PH',
        providers: Optional[List[str]] = None,
        generator: Optional[Generator] = None,
        includes: Optional[List[str]] = None,
        use_weighting: bool = True,
        **config: Any
    ) -> None:
        super().__init__(
            locale, providers, generator, includes, use_weighting, **config
        )

    def random_string(self, length: int = 10):
        letters_count = self.random_int(max=length)
        letters = self.random_letters(letters_count)
        numbers = [str(self.random_digit()) for _ in range(length - letters_count)]
        return ''.join(self.random_elements(letters + numbers, length, True))

    def image(self, size: tuple[int, int] = (1, 1)) -> ContentFile:
        extension = self.file_extension(category='image')
        return ContentFile(
            self.__getattr__('image')(size=size, image_format=extension),
            fake.file_name(category='image', extension=extension),
        )


class Faker(_FactoryFaker):
    @classmethod
    def _get_faker(cls, locale=None):
        if locale is None:
            locale = cls._DEFAULT_LOCALE

        if locale not in cls._FAKER_REGISTRY:
            sub_faker = SubFaker(locale=locale).unique
            cls._FAKER_REGISTRY[locale] = sub_faker

        return cls._FAKER_REGISTRY[locale]


fake: Final[SubFaker] = SubFaker()
