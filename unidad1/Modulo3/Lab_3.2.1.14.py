'''
Nombre: Juan Pablo Ramirez Salazar
Descripcion: Lab 3.2.1.14
Fecha: 26/09/2024
'''
blocks = int(input("Ingresa el número de bloques: "))

height = 0
blocks_used = 0

while blocks_used + (height + 1) <= blocks:
    height += 1  
    blocks_used += height  

print("La altura de la pirámide es:", height)

