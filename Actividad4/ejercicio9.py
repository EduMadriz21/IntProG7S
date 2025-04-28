num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 == num2 == num3:
    print("Los números son iguales")
elif num1 >= num2:
    if num1 >= num3:
        print(f"El mayor es: {num1}")
    else:
        print(f"El mayor es: {num3}")
else:
    if num2 >= num3:
        print(f"El mayor es: {num2}")
    else:
        print(f"El mayor es: {num3}")