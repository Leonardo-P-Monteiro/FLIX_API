from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        
        rate = obj.reviews.aggregate(Avg('stars'))
        result = rate['stars__avg']

        if result: 
            return round(result, 2)
        else:
            return None

    def validate_release_date(self, value):
        if value.year < 1_900:
            raise serializers.ValidationError('A data de lançamento não pode \
ser inferior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 1_000:
            raise serializers.ValidationError('O resumo do filme não pode ser \
superior a 200 caracteres.')
        
        return value

class MovieStatsSerializer(serializers.Serializer):

    # FIELDS OF MY SERIALIZER
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.DecimalField(decimal_places=2, max_digits=5)