rango_inicial = int(input("Escribe el inicio del rango: "))
rango_final = int(input("Escribe el fin del rango: "))

numero = int(input("Dime un numero: "))
if(numero >= rango_inicial and numero <= rango_final):
    print("El numero esta dentro del rnago.")
else: 
    print ("El numero esta fuera del rango")