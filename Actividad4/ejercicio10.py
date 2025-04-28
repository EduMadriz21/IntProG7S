dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes (1-12): "))
anio = int(input("Ingresa el año: "))

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

fecha_valida = True

if mes < 1 or mes > 12:
    fecha_valida = False
elif mes == 2:  
    if es_bisiesto(anio):
        if dia > 29:
            fecha_valida = False
    else:
        if dia > 28:
            fecha_valida = False
elif mes in [4, 6, 9, 11]:  
    if dia > 30:
        fecha_valida = False
else:  
    if dia > 31:
        fecha_valida = False

if fecha_valida:
    print(f"La fecha {dia}/{mes}/{anio} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{anio} NO es válida.")