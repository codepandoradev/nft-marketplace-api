from django.urls import path
from app.games.views import AddPointsView
from app.games.views import MeUserPointsView
from app.games.views import UsersPointsView

urlpatterns = [
    path("add_points/", AddPointsView.as_view()),
    path("me/", MeUserPointsView.as_view()),
    path("", UsersPointsView.as_view()),
]
