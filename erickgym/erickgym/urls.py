from django.urls import path, include
from cadastro.views import ListCreateAlunoView, DetailUpdateDeleteAlunosView

urlpatterns = [
    path('', include('treinos.urls')),
    path('alunos', ListCreateAlunoView.as_view()),
    path('alunos/<int:pk>', DetailUpdateDeleteAlunosView.as_view()),
]
