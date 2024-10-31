#Programa que pida un número y diga si es positivo, negativo o 0.

num = int(input("Digita el numero: "))

if num >= 1:
    print("El número", num, "es POSITIVO")
elif num < 0: 
    print("El número", num, "es NEGATIVO")  
else:
    print("El numero", num,  "es NEUTRO")