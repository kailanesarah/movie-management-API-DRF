from rest_framework import serializers
from movies.models import Movies


class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):

        result = obj.reviews.all()

        print(result)

        if result:
            sum_reviews = 0

            for review in result:
                sum_reviews += review.stars

            reviews_count = result.count()

            return sum_reviews / reviews_count

        

    # o padrão é validade_nome_do_campo_no_model
    # o value já é o campo escolhido, não um objeto, mas o valor do campo em si

    def validate_release_date(self, value):
        print("Valor do campo release_date recebido:", value)

        if value.year < 1990:
            raise serializers.ValidationError(
                'Filmes feitos antes de 1990 não são permitidos')

        return value
