archivo=open("C:\\python\\algoritmos\\notas.txt","w")

for linea in range(3):
    nombre=input("Ingrese el nombre del estudiante: ")
    nota=input("Ingrese la nota del estudiante: ")
    archivo.write(f"{nombre} - {nota}\n")
archivo.close()