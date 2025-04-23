#Solicite al usuario que ingrese la velocidad 
velocidad = float(input("Ingrese la velocidad del vehiculo (km/h): "))

#Verificar si la velocidad supera el limite de 120 km/h
if velocidad > 120: 
    print("Reduzca la velocidad :)")

if velocidad < 120:
    print("Estas dentro del limite :)")

