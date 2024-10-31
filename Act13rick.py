#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.

dia=int(input(f"INGRESA EL DIA DE LA SEMANA (-7)"))
print("\n .LUNES  2.MARTES 3.MIERCOLES  \n 4,JUEVES 5.VIERNES \n 6.SABADO 7.DOMINGO")

dias= {
    1: "LUNES",
    2: "MARTES",
    3: "MIERCOLES",
    4: "JUEVES",
    5: "VIERNES",
    6: "SABADO",
    7: "DOMINGO"
}
if 1 <= dia <= 7:
    print(f"El dia que seleccionaste es el dia: ",dias[dia])
else:
    print(f"ERROR, Ingresa otro numero")