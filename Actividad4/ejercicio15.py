puntos = float(input("Ingresa la puntuación (0-10): "))

if puntos < 0 or puntos > 10:
    print("Error: La puntuación debe estar entre 0 y 10.")
else:
    if puntos >= 9:
        categoria = "Excelente"
    elif puntos >= 7:
        categoria = "Bueno"
    elif puntos >= 5:
        categoria = "Regular"
    else:
        categoria = "Deficiente"
    print(f"\nTu conducta es: {categoria}")