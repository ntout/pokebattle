from django.urls import path
from . import views


urlpatterns = [
    path('battle/', views.BattleDetail.as_view(), name='new_battle'),
    path('battle/<int:battle_id>/', views.BattleDetail.as_view(), name='battle'),
    path('battles/', views.BattleList.as_view(), name='battles'),
    path('pokemon/<pokedex>/', views.PokemonList.as_view(), name='pokemon'),
    path('moves/<pokemon>/', views.MoveList.as_view(), name='moves'),
    path('moves/attr/<move>/', views.MoveDetail.as_view(), name='move'),
]