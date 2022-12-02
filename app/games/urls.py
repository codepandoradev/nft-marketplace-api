from django.urls import path

from app.games.views import GamesAddPointsView, GamesMeView, GamesView, LeadersView

urlpatterns = [
    path('add_points/', GamesAddPointsView.as_view()),
    path('me/', GamesMeView.as_view()),
    path('', GamesView.as_view()),
    path('leaders/', LeadersView.as_view()),
]
