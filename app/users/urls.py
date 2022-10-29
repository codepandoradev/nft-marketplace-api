from django.urls import path

from .views import *

urlpatterns = [
    path('me/', UsersMeView.as_view()),
    path('token/', UsersTokenView.as_view()),
    path('web3/login/', UsersWeb3LoginView.as_view()),
    path('force_login/', UsersForceLoginView.as_view()),
]
