temperatura = float(input("Ingresa la temperatura del servidor (°C): "))
uso_cpu = float(input("Ingresa el porcentaje de uso del CPU (%): "))

if temperatura > 80 or uso_cpu > 95:
    print("ALERTA: Condiciones extremas detectadas.")
    print(" Acción: Iniciando protocolo de emergencia...")
else:
    print("El servidor funciona dentro de los parámetros normales.")