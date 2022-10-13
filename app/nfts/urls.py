from django.urls import path

from .views import *

urlpatterns = [
    path('nfts/', NftsView.as_view())
]
