from django.db.models import Avg, Count
from rest_framework import generics, response, status
from rest_framework.views import APIView
from movies.models import Movies
from movies.serializers import MoviesSerializers, SerializerState
from rest_framework.permissions import IsAuthenticated
from review.models import Review
from app.permissions import GlobalDefaultPermission


class MoviesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movies.objects.all().select_related('genre').prefetch_related('actors')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoviesSerializers
        return MoviesSerializers


class MoviesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers


class MovieStateView(APIView):
    permission_classes = (IsAuthenticated,)
    query_movie = Movies.objects.all()
    query_review = Review.objects.all()

    def get(self, request):
        total_movies = self.query_movie.count()
        movies_by_genre = self.query_movie.values(
            'genre__name').annotate(count=Count('id'))
        total_reviews = self.query_review.count()
        average_stars = self.query_review.aggregate(
            average_stars=Avg('stars'))['average_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }

        serializer = SerializerState(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.validated_data, status=status.HTTP_200_OK)
