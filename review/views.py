from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from review.models import Review
from review.serializers import ReviewSerializers
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class ReviewCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    
class ReviewUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
