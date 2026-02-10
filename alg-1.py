
# Algoritmo (pasos)
# 1. Leer lado
# 2. Calcular perimetro = 4 * lado
# 3. Calcular area = lado ^ 2
# 4. Calcular diagonal = lado * sqrt(2)
# 5. Mostrar resultados

# Diagrama de Flujo
# https://shorturl.at/yBkPb

def main():
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    op = input("Operacion (1 suma, 2 resta, 3 mult, 4 div): ")

    if op == "1":
        print("Resultado:", a + b)
    elif op == "2":
        print("Resultado:", a - b)
    elif op == "3":
        print("Resultado:", a * b)
    elif op == "4":
        if b == 0:
            print("No se puede dividir entre 0")
        else:
            print("Resultado:", a / b)
    else:
        print("Operacion no valida")

if __name__ == "__main__":
    main()

