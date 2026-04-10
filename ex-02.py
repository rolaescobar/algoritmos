import requests

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Lista de Pokémon:\n")

    for i, pokemon in enumerate(data["results"], start=1):
        print(f"{i}. {pokemon['name']}")
else:
    print("Error al conectar con la API")