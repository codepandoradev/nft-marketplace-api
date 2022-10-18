from django.urls import path

from .views import *

urlpatterns = [
    path('', CollectionsView.as_view()),
    path('<str:pk>/', CollectionView.as_view())
]
