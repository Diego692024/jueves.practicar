nombre = "Diego "
sexo = "M"

grupo = ""

if (sexo == "F" and nombre[0].upper() < "M") or (sexo == "M" and nombre[0].upper() > "N"):
    grupo = "A"
else:
    grupo = "B"

print("Usted pertenece al grupo", grupo)