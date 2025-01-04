import requests
import time

URL = "https://api.pokemonbattle.ru/v2"
HEADER = {
    "Content-type" : "application/json",
    "trainer_token" : "53b385269210588bdb7dd0976fb0bbfc"
    }

body_pokemons_POST = {
    "name": "ИГАРЬ",
    "photo_id": -1
}

body_pokemons_PUT = {
    "pokemon_id": "179256",
    "name": "Игорь",
    "photo_id": -1
}

response_one = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons_POST)
response_two = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons_PUT)
response_three = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = { "pokemon_id": "179256" })

print(response_one.text)
time.sleep(2)
print(response_two.text)
time.sleep(2)
print(response_three.text)