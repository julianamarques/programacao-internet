from django.contrib import admin
from django.urls import path
from .views import view_index, view_questions

urlpatterns = [
    path('', view_index),
    path('questions/<int:id>', view_questions),
]