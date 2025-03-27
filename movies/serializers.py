from rest_framework import serializers
from movies.models import Movies
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializers


class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        result = obj.reviews.all()

        if result:
            sum_reviews = 0

            for review in result:
                sum_reviews += review.stars
            reviews_count = result.count()

            return sum_reviews / reviews_count

    def validate_release_date(self, value):
        print("Valor do campo release_date recebido:", value)

        if value.year < 1990:
            raise serializers.ValidationError(
                'Filmes feitos antes de 1990 não são permitidos')

        return value


class DataSerializer(serializers.Serializer):

    genre = GenreSerializer()
    actors = ActorSerializers(many=True)

    class Meta:
        model = Movies
        fields = '__all__'


class SerializerState(serializers.Serializer):
    model = Movies

    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField(source='genre__name')
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
