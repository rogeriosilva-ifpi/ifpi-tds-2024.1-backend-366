from django.contrib import admin
from django.urls import path, include
from core.views import ListCreateEstado, DetailUpdateDeleteEstado


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/estados', ListCreateEstado.as_view()),
    path('api/estados/<int:pk>', DetailUpdateDeleteEstado.as_view())
]
