import pytest
import requests

URL = "https://api.pokemonbattle.ru/v2"
HEADER = {
    "Content-type" : "application/json",
    "trainer_token" : "53b385269210588bdb7dd0976fb0bbfc"
    }

trainer_id = "20408"

def test_status():
    response = requests.get(url = f'{URL}/trainers', params = { "trainer_id" : trainer_id })
    assert response.status_code == 200
    
def test_pokemons():
    response_pokemons = requests.get(url = f'{URL}/trainers', params = { "trainer_id" : trainer_id })
    assert response_pokemons.json()["data"][0]["name"] == 'Игорь'