from django.urls import path

from .views import CollectionsView, CollectionView

urlpatterns = [
    path('', CollectionsView.as_view()),
    path('<str:pk>/', CollectionView.as_view()),
]
