from django.urls import path

from .views import EchoView

urlpatterns = [path('echo/', EchoView.as_view())]
