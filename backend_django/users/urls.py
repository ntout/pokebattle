from unicodedata import name
from django.urls import URLPattern, path
from rest_framework_simplejwt import views as jwt_views
from .views import HelloWorldView, ObtainTokenPair, UserCreate

urlpatterns = [
    path('create/', UserCreate.as_view(), name='create_user'),
    path('token/obtain/', ObtainTokenPair.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world')
]