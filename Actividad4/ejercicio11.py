precio = float(input("Ingresa el precio del producto: "))
saldo = float(input("Ingresa tu saldo disponible: "))


if saldo >= precio:
    print("Compra permitida. ¡Disfruta tu producto!")
else:
    print("Saldo insuficiente.")