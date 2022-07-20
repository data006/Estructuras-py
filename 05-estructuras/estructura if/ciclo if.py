
"""

ESTRUCTURA ALGORITMICA SELECTIVA

sintaxis:
estructura if simple:
    if{condicion}:
        codigo
    else:
        codigo

estructura if multiple:
    if{condicion}:
        codigo
    elif{condicion}:
        codigo
    else:
        codigo

"""

print("\tIf simple")
num = int(input("Ingresa un numero entero: "))

if bool(num%2):
    print("El numero es IMPAR")
else:
    print("El numero es PAR")




print("\n\tIf anidado")
edad = int(input("Ingresa tu edad: "))
continente = input("Cual es tu continente: ")

if edad <= 17:
    print("Aun no eres mayor")
elif edad >= 18:
    if continente.upper() == "AMERICA":
        print("ya eres mayor")
    elif continente.upper() == "ASIA":
        if edad >= 21:
            print("ya eres mayor")
        else:
            print("no eres mayor")
