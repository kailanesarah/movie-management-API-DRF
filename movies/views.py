from django.shortcuts import render
from rest_framework import generics
from movies.models import Movies
from movies.serializers import MoviesSerializers
from rest_framework.permissions import IsAuthenticated

class MoviesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
    
class MoviesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
