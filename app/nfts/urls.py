from django.urls import path

from .views import *

urlpatterns = [
    path('', NftsView.as_view())
]
