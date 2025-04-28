edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 11:
    categoria = "Niño"
elif edad >= 12 and edad <= 17:
    categoria = "Adolescente"
elif edad >= 18 and edad <= 64:
    categoria = "Adulto"
elif edad >= 65:
    categoria = "Adulto mayor"
else:
    categoria = "Edad inválida (ingresa un número positivo)"


print(f"\nTu categoría de edad es: {categoria}")