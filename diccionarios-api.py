import requests

def obtener_pokemon(nombre_o_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id.lower()}"
    
    try:
        response = requests.get(url)
        
        # Si la respuesta es 200 (OK)
        if response.status_code == 200:
            datos = response.json()
            
            print(f"--- Datos de {datos['name'].capitalize()} ---")
            print(f"ID: {datos['id']}")
            print(f"Altura: {datos['height']}")
            print(f"Peso: {datos['weight']}")
            
            # Extraer tipos
            tipos = [t['type']['name'] for t in datos['types']]
            print(f"Tipo(s): {', '.join(tipos)}")
            
        elif response.status_code == 404:
            print("Error: Pokémon no encontrado.")
        else:
            print(f"Error inesperado: {response.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error de conexión: {e}")

# Ejecutamos el ejemplo con Ditto
obtener_pokemon("ditto")