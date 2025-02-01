from django.contrib import admin
from movies.models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'release_date', 
        'genre'
        )
    
