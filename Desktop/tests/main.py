import requests
import json
import time

URL = 'DOMEIN'

HEADER = {
    "Content-type": "application/json",
    "trainer_token": "TRAINER_TOKEN"
}

pokemon_data = {
    "name": "Игорь",
    "photo_id": -1
}

def create_pokemon():
    print("--------------Создание_покемеона--------------")
    time.sleep(3)
    for i in range(3):
        requests_create_pokemons = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=pokemon_data)
        result = requests_create_pokemons.json()

        if result.get("status") == "error" and result.get("message") == "Максимум 5 живых покемонов":
            print("Достигнут лимит на количество покемонов")
            break
        else:
            print(f"Запрос номер {i + 1}: {result}")

def battle():
    print("--------------Получение_списка_моих_покемеонов--------------")
    time.sleep(3)
    requests_list_pokemons = requests.get(url=f'{URL}/v2/pokemons', headers= HEADER, params= {"trainer_id": 20408, "in_pokeball": 0, "status": 1})
    list_json = requests_list_pokemons.json()

    print(json.dumps(list_json, indent=4, ensure_ascii=False))

    print("--------------Добавляю_моих_покеменов_в_покебол--------------")
    time.sleep(3)

    id_pokemon = [pokemon['id'] for pokemon in list_json['data'][:3]]

    for pokemons_in_pokebols in id_pokemon:
        response_in_pokebols = requests.post(url= f'{URL}/v2/trainers/add_pokeball', headers= HEADER, json= {"pokemon_id": pokemons_in_pokebols})
        print(response_in_pokebols.text)

    print("--------------Провожу_битву--------------")
    time.sleep(3)

    request_list_opponent = requests.get(url= f'{URL}/v2/pokemons', headers= HEADER, params={"in_pokeball": 1})
    list_opponent_json = request_list_opponent.json()
    
    id_pokemons_opponent = [pokemon_opponent['id'] for pokemon_opponent in list_opponent_json['data'] if pokemon_opponent['trainer_id'] != "20408"]


    for pokemons_in_pokebols in id_pokemon:
        for battle_opponent in id_pokemons_opponent:
            if pokemons_in_pokebols != battle_opponent:
                requests_battle = requests.post(url= f'{URL}/v2/battle', headers= HEADER, json= {"attacking_pokemon": pokemons_in_pokebols, "defending_pokemon": battle_opponent})
                result_request_battle = requests_battle.json()

                if result_request_battle.get("status") == "error" or result_request_battle.get("message") == "Данный покемон в нокауте":
                    pass
                else:
                    print(requests_battle.text)



create_pokemon()
battle()