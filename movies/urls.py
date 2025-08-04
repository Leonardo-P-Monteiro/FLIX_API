from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from django.urls import path

urlpatterns = [
    path('movie/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movie/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(),
        name='movie-detail-view'),
]
