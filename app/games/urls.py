from django.urls import path

from app.games.views import AddPointsView, MeUserPointsView, UsersPointsView

urlpatterns = [
    path("add_points/", AddPointsView.as_view()),
    path("me/", MeUserPointsView.as_view()),
    path("", UsersPointsView.as_view()),
]
