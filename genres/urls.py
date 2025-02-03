from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name="genre_list_create_view"),
    path('genres/<int:pk>/', views.GenreUpdateDeleteView.as_view(), name="genre_detail_update_deletele_view"),
]


