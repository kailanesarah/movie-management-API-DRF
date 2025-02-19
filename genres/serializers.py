from rest_framework import serializers
from genres.models import Genres


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genres
        fields = '__all__'

    def validate_name(self, value):
        forbidden_genres = ["Pornografia", "Violência Sexual", "Violência", "Terror"]

        if value in forbidden_genres:
            raise serializers.ValidationError('Filmes com esses gêneros não são permitidos')
        
        return value