# 1. Definición: Nombre de la fruta (Clave) y Cantidad (Valor)
inventario = {
    "manzanas": 50,
    "bananos": 120,
    "naranjas": 80
}

# --- RECORRIDO 1: Solo los nombres (Claves) ---
print("Frutas disponibles:")
for fruta in inventario.keys():
    print(f"- {fruta}")

print("\n" + "-"*20 + "\n")

# --- RECORRIDO 2: Solo las cantidades (Valores) ---
total_piezas = 0
for cantidad in inventario.values():
    total_piezas += cantidad

print(f"Total de productos en bodega: {total_piezas}")

print("\n" + "-"*20 + "\n")

# --- RECORRIDO 3: Nombre y Cantidad (Ítems) ---
print("Reporte de Inventario:")
for fruta, cantidad in inventario.items():
    print(f"Hay {cantidad} unidades de {fruta}.")