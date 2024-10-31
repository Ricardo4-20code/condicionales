#Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1=float(input(f"Ingresa el PRIMER numero a DIVIDIR: "))
num2=float(input(f"Ingresa el SEGUNDO numero a DIVIDIR: "))

if num2 != 0:
  division= num1 / num2
  print(f"La division de {num1} entre {num2} es igual a: {division}")
else:
  print(f"El numero que ingresaste es 0, INGRESA otro numero")
