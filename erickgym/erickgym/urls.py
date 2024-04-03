from django.urls import path, include

urlpatterns = [
    path('', include('treinos.urls')),
    path('', include('cadastro.urls')),
    path('', include('auth.urls')),
]
