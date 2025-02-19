from django.db import models
from movies.models import Movies
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[
        MaxValueValidator(5, 'Avaliação máxima com 5 estrelas'),
        MinValueValidator(0, 'Avaliação mínima com 0 estrelas')
    ])
    comment = models.TextField(max_length=150, null= True, blank=True)
