from movies.views import MovieCreateListView, \
    MovieRetrieveUpdateDestroyView, MovieStatsView
from django.urls import path

urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
        name='movie-detail-view'),
    path('movies/statcs/', MovieStatsView.as_view(), name='movie-stats-view')
]
