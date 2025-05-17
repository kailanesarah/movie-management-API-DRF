from rest_framework import serializers
from movies.models import Movies
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializers


class MoviesSerializers(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    actors = ActorSerializers(many=True, read_only=True)

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'  # inclui 'name', 'release_date', 'genre', 'actors', 'resume'

    def get_rate(self, obj):
        result = obj.reviews.all()
        if result:
            sum_reviews = sum([review.stars for review in result])
            reviews_count = result.count()
            return sum_reviews / reviews_count

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                'Filmes feitos antes de 1990 não são permitidos')
        return value


class SerializerState(serializers.Serializer):
    model = Movies

    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField(source='genre__name')
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
