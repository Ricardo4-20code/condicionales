# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

user = str(input(f"INGRESA TU NOMBRE DE USUARIO: "))
password = str(input(f"INGRESA TU CONTRASEÑA: "))

if user == "pepe" and password == "asdasd" :
    print(f"BIENVENIDO Pepe, Has entrado al sistema")
elif user != "pepe" and password != "asdasd":
    print(f"Lo sentimos {user}, tu USUARIO y CONTRASEÑAS son INCORRECTOS")
else:
    print(f"Ingresa tus datos")