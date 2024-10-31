# Escribe un programa que lea un número e indique si es par o impar.

print("PROGRAMA QUE INDICA SI EL NUMERO ES PAR O IMPAR")
numero = int(input("Ingrese un número: "))

if numero % 2 == 0: ## el % divide entre dos y si es igual a cero es par
    print("El número es par.")
    
else:
    print("El número es impar.")