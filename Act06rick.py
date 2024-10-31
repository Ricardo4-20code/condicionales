#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

#len(cadena) == 1 asegura que el usuario haya ingresado solo un carácter.
#cadena.isalpha() verifica que el carácter sea una letra.
#cadena.isupper() comprueba si la letra está en mayúscula.

# Solicitar al usuario que ingrese una cadena
cadena = input("Ingrese una letra: ")

# Verificar si la cadena es una letra mayúscula
if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print("Es una letra mayúscula.")
else:
    print("No es una letra mayúscula.")
