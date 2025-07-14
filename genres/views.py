from django.http import JsonResponse
from genres.models import Genre

# Create your views here.
def genre_view(request):
    """
    Consulta os gêneros existentes no banco de dados.
    """
    genres = Genre.objects.all()
    genres_dict = list(genres.values())
    data = [{'id':genre.id,'name':genre.name} for genre in genres]
    
    return JsonResponse(genres_dict, safe=False)




