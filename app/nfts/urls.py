from django.urls import path

from .views import NftsView

urlpatterns = [path('', NftsView.as_view())]
