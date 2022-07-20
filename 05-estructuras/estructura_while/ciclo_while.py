
num = range(10)
print(len(num))
mi_string = "Hola Mundo!!!"
print(len(mi_string))

i = 0
while i < len(num):
    print(i)
    i+=1
print("Fin del ciclo while")



i=0
while i < len(mi_string):
    print(mi_string[i],end="")
    i+=1
    if i == 5:
        print("saliendo del ciclo")
        break
print()
print("Fin del ciclo while con string")



i=0
while i < 10:
    i += 1

    if i == 2 or i == 3:
        continue
    elif i >=5:
        break

    
    print(i)

    
        

print()
print("Fin del ciclo while con break y continue")

