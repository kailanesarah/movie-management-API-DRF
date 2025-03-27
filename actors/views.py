from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorSerializers
from app.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated
class ActorsCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializers

class ActorsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializers
