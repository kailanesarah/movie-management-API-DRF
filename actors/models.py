from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brazil'),
    ('DEU', 'Alemanha'),
    ('CAN','Canadá'),
    ('CHN','China')
)

class Actors (models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    nationality = models.CharField(choices= NATIONALITY_CHOICES, max_length=100)

    def __str__(self):
        return self.name