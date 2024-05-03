# dada una lista de edades mostrar las que son 
# Menores de edad y las que son Mayores de edad 

edades = [3, 45, 17, 33, 12, 34, 22, 10, 28]

for edad in edades:
    if edad>=18:
        print(f"{edad} Es mayor de edad")
    elif edad >= 5 and edad < 18:
        print(f"{edad} Es niña (o)")
    else:
        print(f"{edad} Es infante")