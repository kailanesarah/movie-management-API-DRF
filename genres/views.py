from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genres
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    
class GenreUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    