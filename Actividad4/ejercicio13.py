saldo = float(input("Ingresa tu saldo inicial: $"))

print("\n--- Menú de Operaciones ---")
print("1. Vaciar cuenta")
print("2. Depositar")
print("3. Retirar")
opcion = int(input("Selecciona una opción (1-3): "))

if opcion == 1:
    saldo = 0
    print("\n Cuenta vaciada. Saldo actual: $0")
elif opcion == 2:
    deposito = float(input("\nIngresa el monto a depositar: $"))
    if deposito > 0:
        saldo += deposito
        print(f"\n Depósito exitoso. Saldo actual: ${saldo:.2f}")
    else:
        print("\n Error: El monto debe ser positivo.")
elif opcion == 3:
    retiro = float(input("\nIngresa el monto a retirar: $"))
    if retiro > saldo:
        print("\n Error: Saldo insuficiente.")
    elif retiro <= 0:
        print("\n Error: El monto debe ser positivo.")
    else:
        saldo -= retiro
        print(f"\n Retiro exitoso. Saldo actual: ${saldo:.2f}")
else:
    print("\n Opción inválida. Inténtalo de nuevo.")