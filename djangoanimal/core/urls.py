from django.urls import path
from core.views import saudacao

urlpatterns = [
    path('saudacao', saudacao),
]