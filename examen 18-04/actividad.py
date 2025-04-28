list_materias = []

for i in range(1, 5):
    materia = input("Ingrese las materias: ")
    list_materias.append(materia)
print(list_materias)

while True:
    respuesta = input("¿Desea agregar otra materia? (si/no): ")
    if respuesta == "si":
        materia = input("Ingrese la materia: ")
        list_materias.append(materia)
        print(list_materias)
    elif respuesta == "no":
        break

while True:
    respuesta = input("¿Desea eliminar una materia? (si/no): ")
    if respuesta == "si":
        materia = input("Ingrese la materia a eliminar: ")
        if materia in list_materias:
            list_materias.remove(materia)
            print(list_materias)
        else:
            print("La materia no está en la lista.")
    elif respuesta == "no":
        break