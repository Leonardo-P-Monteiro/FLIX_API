import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpRequest
from genres.models import Genre
from django.shortcuts import get_object_or_404
from genres.serializers import GenreSerializer
# DRF
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# MY IMPORTS
from app.permissions import GlobalDefaultPermissions

# Create your views here.

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# @csrf_exempt
# def genre_create_list_view(request: HttpRequest) -> JsonResponse:
   
#     if request.method == 'GET':
#         """
#         Consulta os gêneros existentes no banco de dados.
#         """
#         genres = Genre.objects.all()
#         genres_dict = list(genres.values())

#         return JsonResponse(genres_dict, safe=False, status= 200)

#     elif request.method == 'POST':
#         """
#         Cria gêneros no banco de dados.
#         """
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()

#         return JsonResponse(
#             {
#                 'id':new_genre.pk,
#                 'name':new_genre.name
#             }, 
#             status=201,
#         )
    
#     return JsonResponse({'error': 'Method not allowed'}, status=405)

# @csrf_exempt
# def genre_detail_view(request: HttpRequest, pk:int) -> JsonResponse:
#     """
#     Acessando detalhes de um único item do banco de dados.
#     """
#     genre_obj = get_object_or_404(Genre, pk=pk)

#     # MÉTODO GET - CONSULTA
#     if request.method == "GET":
        
#         data = {
#             'id': genre_obj.pk,
#             'name': genre_obj.name
#         }

#         return JsonResponse(data=data, status=200)

#     # MÉTODO PUT - SUBSTITUIÇÃO/ALTERAÇÃO
#     elif request.method == "PUT":

#         data = json.loads(request.body.decode('utf-8'))
#         genre_obj.name = data['name']
#         genre_obj.save()

#         data = {
#             'id': genre_obj.pk,
#             'name': genre_obj.name
#         }

#         return JsonResponse(data, status=201)
    
#     # MÉTODO DELETE - EXCLUSÃO DE INFORMAÇÕES
#     elif request.method == "DELETE":
#         genre_obj.delete()
        
#         return JsonResponse({'message':'Delete process success'}, status=204)
    
#     return JsonResponse({'erro':'Method not allowed'}, status=405)