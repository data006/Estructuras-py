
num = range(10)
print(type(num))

#EJEMPLO CICLO FOR CON NUMEROS DECLARADOS
for i in 1,2,3:
    print(i)



print("Ciclo for con funcion Range")
#EJEMPLO CICLO FOR CON RANGE
for i in range(0,10):
    if i==7:
        print("Saliendo del  ciclo")
        break
    elif i==2 or i==4:
        continue
    else:
        print(i)



#EJEMPLO CICLO FOR CON NUMEROS DECLARADOS CON CIERTOS INTERVALOS
for j in range(0,110,10):
    print(j)



print("Ciclo for con dato String")
#EJEMPLO CICLO FOR CON NUMEROS DECLARADOS
nombre = "Carlos Salas"
for l in nombre:
    #print(l)
    print(l,end="")
