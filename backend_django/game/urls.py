from django.urls import path
from . import views


urlpatterns = [
    path('', views.users, name = 'users'),
    path('battle/', views.simulate_battle, name = 'battle')
]