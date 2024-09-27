'''
Nombre: Juan Pablo Ramirez Salazar
Descripcion: Lab 3.1.1.12
Fecha: 26/09/2024
'''
# Entrada: año a verificar
año = int(input("Introduce un año: "))

if año < 1582:
    print("No está dentro del período del calendario Gregoriano")
else:
    if año % 4 != 0:
        print("Año Común")
    elif año % 100 != 0:
        print("Año Bisiesto")
    elif año % 400 != 0:
        print("Año Común")
    else:
        print("Año Bisiesto")

