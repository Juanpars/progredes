'''
Descripción del ejercicio: Manejo de listas en Python
Nombre del participante: Juan Pablo Ramirez Salazar
Fecha de creación: 03/10/2024
Tema: Manejo de listas
'''

# 3. Realizar un salto de línea (puedes usar "\n" en los prints para esto)
print("\n")

# 4. Crear una lista con cuatro compañeros
nombres = ['Francisco', 'Pedro', 'Juan', 'Fernando']

# 5. Desplegar el tamaño de la lista
print("El tamaño en lista es", len(nombres))

# 6. Desplegar el contenido de la lista
print("El contenido en lista es", nombres)

# 7. Cambiar el segundo elemento de la lista por “Joaquín”
nombres[1] = 'Joaquín'

# 8. Agregar el nombre "Luis Miguel" a la lista
nombres.append('Luis Miguel')

# 9. Eliminar el tercer elemento de la lista
nombres.pop(2)

# 10. Desplegar la lista en orden inverso separados con un carácter
print('*'.join(nombres[::-1]))
