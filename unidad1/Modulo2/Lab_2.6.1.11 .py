'''
Nombre: Juan Pablo Ramirez Salazar
Descripcion: Lab 2.6.1.11
Fecha: 19/09/2024
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_mins = mins + dura

additional_hours = total_mins // 60  
final_minutes = total_mins % 60  

final_hour = (hour + additional_hours) % 24  

print(f"El evento termina a las {final_hour}:{final_minutes}")
