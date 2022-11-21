from django.conf import settings
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.views import set_rollback

from .client import ClientError
from .critical import CriticalError
from .warning import APIWarning


def exception_handler(exception):
    try:
        set_rollback()
        if settings.DEBUG and isinstance(exception, MethodNotAllowed):
            return Response(str(exception))
        try:
            raise exception
        except APIWarning as e:
            api_error = e
        except ClientError as e:
            api_error = e
        except CriticalError as e:
            api_error = e
        except tuple(APIWarning.EXCEPTION__CAST.keys()) as exception_to_cast:
            api_error = APIWarning.cast_exception(exception_to_cast)
        except tuple(ClientError.EXCEPTION__CAST.keys()) as exception_to_cast:
            api_error = ClientError.cast_exception(exception_to_cast)
        except tuple(CriticalError.EXCEPTION__CAST.keys()) as exception_to_cast:
            api_error = CriticalError.cast_exception(exception_to_cast)

        error = api_error

    except Exception as e:
        error = CriticalError(str(e))

    error.log()
    return error.to_response()
