# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta

jugador1=str(input("Ingrese la opcion del PRIMER JUGADOR(PIEDRA, PAPEL O TIJERA)"))
jugador2=str(input("Ingrese la opcion del SEGUNDO JUGADOR (PIEDRA, PAPEL O TIJERA)"))


opciones_validas = ["piedra", "papel", "tijera"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas: ##not in: Este operador verifica si un elemento no está presente en una secuencia. Si alguna de las entradas no es válida, se ejecutará el bloque de código correspondiente.
    print("Opción incorrecta: ambos jugadores deben elegir 'piedra', 'papel' o 'tijera'.")
else:
    if jugador1 == jugador2:
        print("Empate.")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("Gana Jugador 1.")
    else:
        print("Gana Jugador 2.")
