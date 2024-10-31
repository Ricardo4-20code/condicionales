#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.
 
duracion=int(input(f"Ingresa la duracion de la llamada en minutos: "))
dia=input(f"Ingresa el dia de la semana: ").lower ##.lower inserta valores en una cadena en lugares especificos 
turno=input(f"Ingresa el turno (mañana/tarde): ").lower

if duracion <= 5:
    costobase= duracion * 1.0
elif duracion <= 8:
    costobase=  5 * 1.0 + (duracion - 5) * 0.8
elif duracion <= 10:
    costobase=  5 * 1.0 + 3 * 0.8 + (duracion - 8) * 0.7
else:
    costobase = 5 * 1.0 + 3 * 0.8 + 2 * 0.7 + (duracion - 10) * 0.5

if dia == "domingo":
    impuesto = costobase * 0.3
elif turno == "mañana":
    impuesto = costobase * 0.15
else:
    impuesto = costobase * 0.10

totalpagar = costobase + impuesto

print("Costo base de la llamada: {:.2f} euros".format(costobase))## :.2f significa que almacena un valor de tipo float
print("Impuesto aplicado: {:.2f} euros".format(impuesto))        ## con dos decimales
print("Total a pagar: {:.2f} euros".format(totalpagar))

##El método .format() permite insertar valores en una cadena de texto en lugares específicos
##Se coloca {} dentro de la cadena donde deseas insertar el valor
## y luego llamas a .format() pasando los valores en el orden correspondiente.