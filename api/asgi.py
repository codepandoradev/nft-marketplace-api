import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

asgi_application = get_asgi_application()

from app.base.middlewares.ws_log import WsLogMiddleware  # noqa:#402
from app.base.urls import ws_urlpatterns as base_ws_urlpatterns  # noqa:#402

application = ProtocolTypeRouter(
    {
        'http': asgi_application,
        'websocket': WsLogMiddleware(URLRouter(base_ws_urlpatterns)),
    }
)
