from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from app.permissions import GlobalDefaultPermissions
from django.db.models import Count, Avg
from reviews.models import Review
from .serializers import MovieStatsSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieStatsView(views.APIView):
    
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get(self, request, *args, **kwargs):

        # FETCH ALL OF DATA
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        
        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars) if average_stars else 0,
        }

        data_serialize = MovieStatsSerializer(data=data)
        data_serialize.is_valid(raise_exception=True)


        # GIVE BACK RESPONSE TO USE AS STATISTICS
        return response.Response(
            status=status.HTTP_200_OK,
            data= data_serialize.validated_data)