from django.db import models
from genres.models import Genres
from actors.models import Actors


class Movies(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ForeignKey(
        Genres, on_delete=models.PROTECT, related_name='movie_genre')
    actors = models.ManyToManyField(Actors, related_name='movie_actors')
    resume = models.TextField(max_length=300, default="Descrição do filme")

    def __str__(self):
        return self.name
