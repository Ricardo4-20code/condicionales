##Un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto

cara=int(input(f"Ingresa el resultado del dado obtenido (1-6)"))

carasop = {
1: "seis",
2: "cinco",
3: "cuatro",
4: "tres",
5: "dos",
6: "uno" }

if 1 <= cara <= 6:
    print(f"La cara opuesta de {cara} es: ", carasop[cara])
else:
    print(f"ERROR: número incorrecto")