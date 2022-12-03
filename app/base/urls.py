from django.urls import path

from .consumers import EchoConsumer
from .views import EchoView, StatusView

urlpatterns = [path('echo/', EchoView.as_view()), path('status/', StatusView.as_view())]

ws_urlpatterns = [
    path('ws/echo/', EchoConsumer.as_asgi()),
]
