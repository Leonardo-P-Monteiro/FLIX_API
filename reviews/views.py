from django.shortcuts import render
from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializer

# Create your views here.

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

