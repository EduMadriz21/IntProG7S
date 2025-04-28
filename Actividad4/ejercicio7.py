monto_total = float(input("Monto total: "))
satisfaccion = input("Ingrese su nivel de satisfaccion (Buena/Mala): ")

if satisfaccion == "Buena": 
    propina = monto_total * 0.15
elif satisfaccion == "Mala": 
    propina =  monto_total * 0.05
else:
    print("Nivel de satisfaccion invalido. Usar 'Buena' o 'Mala' ")
total_pagar = monto_total + propina 

print(f"\nDetalle de pago:")
print(f"Monto inicial: ${monto_total:.2f}")
print(f"Propina ({satisfaccion}): ${propina:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")
    