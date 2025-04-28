#Solicitar al usuario ingresar la edad
edad = int(input("Ingrese la edad de la persona: "))

#Verificar si la persona se puede votar 
if edad >= 18:
    print("Puede votar")
if edad < 18:
    print("No puede votar")