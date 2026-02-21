#PSEUDOCÓDIGO
#1. Solicitar al usuario que ingrese el monto de la compra
#2. Si el monto de la compra es mayor o igual a 100, aplicar un descuento del 10%
#3. Si no:
  #descuento = 0
#4. Mostrar el monto original, descuento y total a pagar 

monto_compra = float(input("Ingrese el monto de la compra: Q"))

if monto_compra >= 100:
    descuento = monto_compra * 0.10
else:     descuento = 0

total = monto_compra - descuento

print("Monto original: Q", monto_compra)
print("Descuento: Q", descuento)
print("Total a pagar: Q", total)




