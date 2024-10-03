'''
# Descripción: Ejercicio sobre el manejo de colecciones en Python
# Autor: Juan Pablo Ramirez Salzar
# Fecha: 03/10/2024
# Tema: Manejo de colecciones y ciclos en Python
'''

#3 Lista vacía para los nombres
nombres = []

#4 Lista de números de control
numeros_control = [1219100524, 1219100537, 1219100543, 1219100583, 1219100844]

#5 Pedir nombres para cada número de control
for numero in numeros_control:
    nombre = input(f"Escribe el nombre para el número de control {numero}: ")
    nombres.append(nombre)

#6 Mostrar la lista de nombres
print("Nombres registrados:", nombres)

#7 Búsqueda de número de control
while True:
    numero_buscado = int(input("Escribe un número de control para buscar: "))
    encontrado = False

    #8 Buscar manualmente el número de control
    for i in range(len(numeros_control)):
        if numeros_control[i] == numero_buscado:
            print(f"El nombre es: {nombres[i]}")
            encontrado = True
            break

    if encontrado:
        break
    else:
        print("Número de control no encontrado. Intenta de nuevo.")
