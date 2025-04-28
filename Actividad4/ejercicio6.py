calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))
if 0 <= calificacion <= 100:
    if calificacion >= 70:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Error: La calificación debe estar entre 0 y 100")