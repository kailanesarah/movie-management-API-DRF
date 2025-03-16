from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genres
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from genres.permissions import GenrePermissionClass



class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    
class GenreUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    