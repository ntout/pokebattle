from django.shortcuts import render
from django.http import HttpResponse
import requests

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