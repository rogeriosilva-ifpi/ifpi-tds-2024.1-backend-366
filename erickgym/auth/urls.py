from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from auth.views import SignupAPIView, SigninAPIView

urlpatterns = [
    path('auth/signup', SignupAPIView.as_view()),
    # path('auth/signin', SigninAPIView.as_view())
    path('auth/signin', ObtainAuthToken.as_view())
]
