from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.ReviewCreateListView.as_view(), name="review_list_create_view"),
    path('review/<int:pk>/', views.ReviewUpdateDeleteView.as_view(), name="review_detail_update_deletele_view"),
]


