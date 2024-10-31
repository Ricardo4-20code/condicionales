##Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

num1=int(input(f"Ingresa el PRIMER numero: "))
num2=int(input(f"Ingresa el SEGUNDO numero: "))
num3=int(input(f"Ingresa el TERCER numero: "))

if num1 > num2 and num1 < num3:
    print(f"El ORDEN de MENOR A MAYOR ES: {num2} {num1} {num3}")

elif num2 > num1 and num2 < num3:
    print(f"El ORDEN de MENOR A MAYOR ES: {num1} {num2} {num3}")

elif num1 == num2 and num2 == num3 and num1 == num3: 
    print(f"Los numeros son iguales: {num1} {num2} {num3}")
else:
    print(f"El ORDEN de MENOR A MAYOR ES: {num3} {num2} {num1}")
