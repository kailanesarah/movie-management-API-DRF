from django.shortcuts import render
from rest_framework import generics
from movies.models import Movies
from movies.serializers import MoviesSerializers

class MoviesCreateListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
    
class MoviesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
