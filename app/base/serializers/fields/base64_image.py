from drf_base64.fields import Base64ImageField as _Base64ImageField
from django_svg_image_form_field import SvgAndImageFormField
from rest_framework.fields import SkipField


# FIXME: add allowed_extensions
# FIXME: add OpenApiSerializerFieldExtension for this
class Base64ImageField(_Base64ImageField):
    def __init__(self,  **kwargs):
        kwargs['_DjangoImageField'] = SvgAndImageFormField
        super().__init__(**kwargs)

    def _decode(self, data):
        try:
            value = super()._decode(data)
        except SkipField:
            if self.required:
                self.fail('invalid_image')
            raise
        except (ValueError, UnicodeDecodeError):
            self.fail('invalid_image')
        return value
