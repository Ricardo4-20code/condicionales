# Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base=float(input(f"INGRESA EL NUMERO A ELEVAR A SU POTENCIA (base): ")) 
exponente=int(input(f"INGRESA EL NUMERO A ELEVAR (exponente)"))

if exponente > 0:
    resultado = base ** exponente
    print("El resultado de la potencia es:", resultado)
elif exponente == 0:
    print("El resultado de la potencia es: 1")
else:
    resultado = 1 / (base ** abs(exponente)) 
    ##si el exponente es negativo se calcula la potencia con el exponente positivo y luego se toma su inverso
    ##la funcion abs()= devuelve el valor absoluto del número especificado
    print("El resultado de la potencia es:", resultado)
