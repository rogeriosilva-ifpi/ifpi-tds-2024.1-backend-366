from django.urls import path
from treinos.views import (
    ListCreateExerciciosView,
    DetailUpdateDeleteExerciciosView)

urlpatterns = [
    path('exercicios', ListCreateExerciciosView.as_view()),
    path('exercicios/<int:pk>', DetailUpdateDeleteExerciciosView.as_view()),
]
