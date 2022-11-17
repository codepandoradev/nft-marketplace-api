from django.urls import path

from .consumers import EchoConsumer
from .views import EchoView

urlpatterns = [
    path('echo/', EchoView.as_view()),
]

ws_urlpatterns = [
    path('echo/', EchoConsumer.as_asgi()),
]
