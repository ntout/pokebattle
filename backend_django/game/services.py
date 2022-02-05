
from .battlelogic import Move
import requests


class PokeApi:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/'
        

    def get_pokemon_list_by_pokedex(self, pokedex):
        url = self.base_url + 'pokedex/' + pokedex
        response = requests.get(url)
        data = response.json()

        pokemon = []
        for p in data['pokemon_entries']:
            pokemon.append({'id':p['entry_number'], 'name':p['pokemon_species']['name']})

        return pokemon


    def get_pokemon_moves(self, pokemon):
        url = self.base_url + 'pokemon/' + str(pokemon)
        response = requests.get(url)
        data = response.json()
        moves = []

        for m in data['moves']:
            moves.append(m['move']['name'])

        return moves


    def get_move_attributes(self, move):
        url = self.base_url + 'move/' + str(move)
        response = requests.get(url)
        data = response.json()

        return Move(move, data['pp'], data['accuracy'], data['power'])


if __name__ == "__main__":
    pokeapi = PokeApi()
    # pokemon = pokeapi.get_pokemon_list_by_pokedex('kanto')
    # pokeapi.get_pokemon_moves('charmander')
    # pokeapi.get_move_attributes('pound')

    