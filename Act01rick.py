#da dos numero a indique cual es el mayor 
## Si los dos son iguales que muestre # Programa que piel mensaje "Son iguales"
num1=int(input(f"Ingresa el primer numero: "))
num2 = int(input( f"Ingresa el segundo numero: "))

if num1 > num2: 
    print("El primer numero es el MAYOR: ",num1)
elif num1 < num2:
    print("El segundo numero es el MAYOR: ",num2)
else:
    print("Los numeros,",num1, "Y" , num2, "son IGUALES")
