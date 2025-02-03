from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorsCreateListView.as_view(), name="actors_list_create_view"),
    path('actors/<int:pk>/', views.ActorsUpdateDeleteView.as_view(), name="actors_detail_update_deletele_view"),
]


