ventas = [120,150,90,200,175]

total = 0

for venta in ventas:
    
    if venta > 150:
        print("************** Alta  *******************")
        print("Venta alta:", venta )
    else:
        print("**************** Normal  ****************")
        print("Venta normal:", venta)

    total = sum(ventas)
    #total = total + venta
print("Total de ventas:", total)

