'''
Nombre: Juan Pablo Ramirez Salazar
Descripcion: Lab 3.4.1.6
Fecha: 26/09/2024
'''
hat_list = [1, 2, 3, 4, 5]  

hat_list[2] = int(input("Ingresa un número entero para reemplazar el número en el centro: "))

hat_list.pop()

print("La longitud de la lista es:", len(hat_list))

print(hat_list)
