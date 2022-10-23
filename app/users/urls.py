from django.urls import path

from .views import *

urlpatterns = [
    # TODO:
#     path('register/', UsersRegisterView.as_view()),
#     path('register/resend/', UsersRegisterResendView.as_view()),
    #     path('password/', UsersPasswordView.as_view()),
    #     path('token/', UsersTokenView.as_view()),
    #     path('me/password/', UsersMePasswordView.as_view()),
    path('me/', UsersMeView.as_view()),
    path('web3/login/', UsersWeb3LoginView.as_view()),
    path('force_login/', UsersForceLoginView.as_view()),
]
