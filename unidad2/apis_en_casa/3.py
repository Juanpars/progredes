import requests

def obtener_chiste(categoria="Any"):
    url = f"https://v2.jokeapi.dev/joke/{categoria}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        chiste = respuesta.json()
       
        if chiste["type"] == "single":
            return chiste["joke"]
    
        elif chiste["type"] == "twopart":
            return f"{chiste['setup']} - {chiste['delivery']}"
    else:
        print("Error al obtener el chiste.")
        return None

print("Categorías disponibles: 'Programming', 'Misc', 'Dark', 'Pun', 'Spooky', 'Christmas'")
categoria = input("Escribe una categoría o 'Any' para chistes de todas las categorías: ")

chiste = obtener_chiste(categoria)
if chiste:
    print(f"\nAquí tienes un chiste: {chiste}")
else:
    print("No se encontró ningún chiste en esa categoría.")
