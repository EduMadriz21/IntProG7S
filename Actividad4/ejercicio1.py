rango_inicial = int(input("Escribe el inicio del rango: "))
rango_final = int(input("Escribe el fin del rango: "))

if(rango_inicial < rango_final): 
        numero = int(input("Dime un numero: "))
        if(numero >= rango_inicial and numero <= rango_final):
            print("El numero esta dentro del rnago.")
        else: 
            print ("El numero esta fuera del rango")
else: 
    print("EL rango inicial debe ser menor que el rango final")

