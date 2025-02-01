from django.shortcuts import render
from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorSerializers


class ActorsCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializers
    
    
class ActorsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializers
    
