from django.urls import path

from app.games.views import GamesAddPointsView, GamesMeView, GamesView

urlpatterns = [
    path('add_points/', GamesAddPointsView.as_view()),
    path('me/', GamesMeView.as_view()),
    path('', GamesView.as_view()),
]
