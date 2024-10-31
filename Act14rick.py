#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.

mes=int(input(f"1.ENERO  2.FEBRERO 3.MARZO 4.ABRIL  \n  5.MAYO 6.JUNIO 7.JULIO 8.AGOSTO \n 9.SEPTIEMBRE 10.OCTUBRE 11.NOVIEMBRE 12.DICIEMBRE\n\n INGRESA EL MES QUE DESEAS (1 - 12):  "))

diasmes = {
    1: 31,   # Enero
    2: 28,   # Febrero 
    3: 31,   # Marzo
    4: 30,   # Abril
    5: 31,   # Mayo
    6: 30,   # Junio
    7: 31,   # Julio
    8: 31,   # Agosto
    9: 30,   # Septiembre
    10: 31,  # Octubre
    11: 30,  # Noviembre 
    12: 31   # Diciembre
}
if mes in diasmes:
    print(f"El mes {mes} tiene {diasmes[mes]} dias")
else:
    print(f"ERROR, ingresa un numero que este en el rango")