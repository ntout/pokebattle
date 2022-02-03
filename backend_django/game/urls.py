from django.urls import path
from . import views


urlpatterns = [
    path('', views.users, name = 'users'),
    path('battle/', views.BattleDetail.as_view(), name='new_battle'),
    path('battle/<int:battle_id>/', views.BattleDetail.as_view(), name='battle'),
    path('battles/', views.BattleList.as_view(), name='battles'),
]