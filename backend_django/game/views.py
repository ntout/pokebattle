from shutil import move
from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .services import PokeApi
from .serializers import BattleSerializer

from rest_framework.permissions import IsAuthenticated

from .models import Battle

from .battlelogic import Pokemon, Move, BattleSimulation


class BattleDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Battle.objects.get(pk=pk)
        except Battle.DoesNotExist:
            raise Http404

    def get(self, request, battle_id: int):
        battle = self.get_object(battle_id)
        serializer = BattleSerializer(battle)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data

        p1: Pokemon = Pokemon(data['pokemon_1'])
        p2: Pokemon = Pokemon(data['pokemon_2'])

        for move in data['moves_1']:
            p1.add_move(Move(move['name'], move['pp'], move['accuracy'], move['power']))
    
        for move in data['moves_2']:
            p2.add_move(Move(move['name'], move['pp'], move['accuracy'], move['power']))

        battle: BattleSimulation = BattleSimulation(p1, p2)
        battle.simulate()
   
        btl: Battle = Battle.objects.create(pokemon_1=battle.poke1.name, pokemon_2=battle.poke2, move_log=battle.move_log, winner=battle.winner)
        serializer = BattleSerializer(btl)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BattleList(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        battles = Battle.objects.all()
        serializer = BattleSerializer(battles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PokemonList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pokedex):
        print(pokedex)
        pokeapi = PokeApi()
        pokemon = pokeapi.get_pokemon_list_by_pokedex(pokedex)
        return Response(data=pokemon, status=status.HTTP_200_OK)


class MoveList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pokemon):
        print(move)
        pokeapi = PokeApi()
        moves = pokeapi.get_pokemon_moves(pokemon)
        return Response(moves, status=status.HTTP_200_OK)


class MoveDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, move):
        print(move)
        pokeapi = PokeApi()
        move = pokeapi.get_move_attributes(move)

        return Response(move.get_data(), status=status.HTTP_200_OK)