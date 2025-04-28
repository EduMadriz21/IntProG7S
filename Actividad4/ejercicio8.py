def verificar_login():
    
    usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su clave: ")
    
    
    if usuario == "admin" and clave == "1234admin":
        print("Acceso permitido")
    else:
        print("Acceso denegado")

verificar_login()