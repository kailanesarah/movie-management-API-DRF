from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MoviesCreateListView.as_view(), name="movies_list_create_view"),
    path('movies/<int:pk>/', views.MoviesUpdateDeleteView.as_view(), name="movies_detail_update_deletele_view"),
]


