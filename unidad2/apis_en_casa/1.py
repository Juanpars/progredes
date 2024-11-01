import requests

def obtener_todas_las_razas():
    url = "https://dog.ceo/api/breeds/list/all"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        razas = respuesta.json()["message"]
        return razas
    else:
        print("Error al obtener la lista de razas.")
        return None

def obtener_imagen_aleatoria(raza):
    url = f"https://dog.ceo/api/breed/{raza}/images/random"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        url_imagen = respuesta.json()["message"]
        return url_imagen
    else:
        print(f"Error al obtener imagen para la raza {raza}.")
        return None


razas = obtener_todas_las_razas()
if razas:
    print("Razas disponibles:")
    for raza in razas.keys():
        print(raza)

    raza_seleccionada = input("Escribe una raza para ver una imagen: ").lower()
    if raza_seleccionada in razas:
        imagen_url = obtener_imagen_aleatoria(raza_seleccionada)
        if imagen_url:
            print(f"Imagen aleatoria de un {raza_seleccionada}: {imagen_url}")
    else:
        print("Raza no encontrada.")

