# Crear un archivo, escribir datos en él y cerrarlo
with open("C:\\python\\algoritmos\\tabla10.txt","w") as archivo:
    for i in range(1, 11):
        linea = f"10 x {i} = {10 * i}\n"
        archivo.write(linea)


# Leer el archivo y mostrar su contenido
with open("C:\\python\\algoritmos\\tabla10.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)
    