from django.urls import path

from .consumers import *
from .views import *

urlpatterns = [
    path('direct/<int:interlocutor>/messages/', MessengerDirectMessagesView.as_view())
]

ws_urlpatterns = [
    path('messenger/direct/<int:interlocutor>/', MessengerDirectConsumer.as_asgi()),
]
