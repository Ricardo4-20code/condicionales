#Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
#y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
#la edad es mayor o igual a dieciocho y el sexo es 'F'. 
#En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
#Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.

nota=float(input(f"Ingresa el valor de tu NOTA: "))
edad=int(input(f"Ingresa tu EDAD: "))
sexo=str(input(f"DIGITA F. si tu sexo es FEMENINO O M. si tu sexo MASCULINO: "))

if nota >= 5 and edad >= 18 and sexo == "f":
    print(f"ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == "m":
    print(f"POSIBLE")
else:
    print(f"NO ACEPTADA")