import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

http_application = get_asgi_application()

from app.base.middlewares.ws_log import WsLogMiddleware  # noqa:#402
from app.base.middlewares.ws_token_auth import TokenAuthMiddleware  # noqa:#402
from app.base.urls import ws_urlpatterns as base_ws_urls  # noqa:#402
from app.messenger.urls import ws_urlpatterns as messenger_ws_urls  # noqa:#402

application = ProtocolTypeRouter(
    {
        'http': http_application,
        'websocket': TokenAuthMiddleware(
            WsLogMiddleware(URLRouter(base_ws_urls + messenger_ws_urls))
        ),
    }
)
