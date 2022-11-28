from django.urls import path

from .views import (
    UsersMeView,
    UsersSessionView,
    UsersTokenView,
    UsersWeb3ForceLoginView,
    UsersWeb3LoginView,
)

urlpatterns = [
    path('me/', UsersMeView.as_view()),
    path('token/', UsersTokenView.as_view()),
    path('session/', UsersSessionView.as_view()),
    path('web3/login/', UsersWeb3LoginView.as_view()),
    path('web3/force_login/', UsersWeb3ForceLoginView.as_view()),
]
