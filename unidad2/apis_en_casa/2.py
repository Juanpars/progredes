import requests

def obtener_todos_los_paises():
    url = "https://restcountries.com/v3.1/all"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        paises = respuesta.json()
        return paises
    else:
        print("Error al obtener la lista de países.")
        return None

def obtener_informacion_pais(pais):
    url = f"https://restcountries.com/v3.1/name/{pais}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        informacion_pais = respuesta.json()[0] 
        return informacion_pais
    else:
        print(f"Error al obtener información para el país {pais}.")
        return None

# Ejemplo de uso
paises = obtener_todos_los_paises()
if paises:
    print("Países disponibles:")
    for pais in paises:
        print(pais["name"]["common"])

    pais_seleccionado = input("Escribe el nombre de un país para ver más información: ").capitalize()
    informacion = obtener_informacion_pais(pais_seleccionado)
    if informacion:
        print(f"\nInformación de {pais_seleccionado}:")
        print(f"Nombre oficial: {informacion['name']['official']}")
        print(f"Capital: {informacion.get('capital', ['No disponible'])[0]}")
        print(f"Región: {informacion['region']}")
        print(f"Población: {informacion['population']}")
        print(f"Área: {informacion['area']} km²")
    else:
        print("País no encontrado.")

