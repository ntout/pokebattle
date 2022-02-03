from django.urls import path
from . import views


urlpatterns = [
    path('', views.users, name = 'users'),
    path('battle/', views.simulate_battle, name='simulate'),
    path('battle/<int:battle_id>/', views.BattleDetail.as_view(), name='battle'),
    path('battles/', views.BattleList.as_view(), name='battles'),
]