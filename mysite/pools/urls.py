from django.contrib import admin
from django.urls import path
from .views import view_index, view_question, view_result

urlpatterns = [
    path('', view_index),
    path('question/<int:id>', view_question),
    path('question/<int:id>/result', view_result),
]