from django.shortcuts import render
from reviews.models import Review
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.serializers import ReviewSerializer
from app.permissions import GlobalDefaultPermissions
# Create your views here.

class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

