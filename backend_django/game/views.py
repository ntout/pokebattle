from shutil import move
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests

from .models import Battle

from .battlelogic import Pokemon, Move, BattleSimulation

# Create your views here.
def users(request):

     #pull data from third party rest api
    response = requests.get('https://pokeapi.co/api/v2/pokedex/2/')

    #convert reponse data into json
    pokedex = response.json()
    print(len(pokedex['pokemon_entries']))

    poke_id = pokedex['pokemon_entries'][69]

    poke_url = 'https://pokeapi.co/api/v2/pokemon/69'
    poke_response = requests.get(poke_url)
    pokemon = poke_response.json()
    print(pokemon['name'])


    return HttpResponse("Users")


@api_view(['GET'])
def getBattles(request):
    pass

@api_view(['POST'])
def addBattle(request):
    pass


def simulate_battle(request):
    p1: Pokemon = Pokemon('Charmander')
    p2: Pokemon = Pokemon('Squirtle')

    m1: Move = Move('Tackle', 25, 80, 15)
    m2: Move = Move('Water Gun', 25, 75, 25)
    m3: Move = Move('Ember', 25, 75, 25)
    m4: Move = Move('Pound', 25, 80, 35)

    p1.add_move(m1)
    p1.add_move(m3)
    p1.add_move(m4)

    p2.add_move(m1)
    p2.add_move(m2)
    p2.add_move(m4)

    battle: BattleSimulation = BattleSimulation(p1, p2)
    battle.simulate()

    
    btl: Battle = Battle.objects.create(pokemon_1=battle.poke1.name, pokemon_2=battle.poke2, move_log=[], winner=battle.winner)
    
    print(len(battle.move_log))
    for log in battle.move_log:
        print(log)
        btl.move_log.append(log)
    btl.save()

    return HttpResponse("battle")