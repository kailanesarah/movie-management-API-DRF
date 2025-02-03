from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from review.models import Review
from review.serializers import ReviewSerializers


class ReviewCreateListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    
class ReviewUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
