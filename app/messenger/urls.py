from django.urls import path

from .consumers import MessengerDirectConsumer

ws_urlpatterns = [
    path('messenger/direct/<int:interlocutor>/', MessengerDirectConsumer.as_asgi()),
]
