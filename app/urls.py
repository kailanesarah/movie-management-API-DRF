from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenrelUpdateDeleteView
from actors.views import ActorsCreateListView, ActorsUpdateDeleteView
from movies.views import MoviesCreateListView, MoviesUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name="genre_list_create"),
    path('genres/<int:pk>/', GenrelUpdateDeleteView.as_view(),
         name="genres_detail_update_delete"),

    path('actors/', ActorsCreateListView.as_view(), name="actors_list_create"),
    path('actors/<int:pk>/', ActorsUpdateDeleteView.as_view(),
         name="actors_detail_update_delete"),

    path('movies/', MoviesCreateListView.as_view(), name="movies_list_create"),
    path('movies/<int:pk>/', MoviesUpdateDeleteView.as_view(),
         name="movies_detail_update_delete")



]
