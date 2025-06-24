Precio_producto=float(input("Ingrese el precio del producto: "))
print("El precio del producto es:", Precio_producto)

Cantidad_producto=int(input("Ingrese la cantidad comprada: "))
print("La cantidad de producto es:", Cantidad_producto)

descuento=float(input("Ingrese el descuento aplicado: "))
print("El descuento aplicado es:", descuento)

Precio_total_sin_descuento = Precio_producto * Cantidad_producto
print("El precio total sin descuento es:", Precio_total_sin_descuento)

Precio_total_con_descuento = [Precio_total_sin_descuento - (0.1 * Precio_total_sin_descuento)]
print("El precio total con descuento es:", Precio_total_con_descuento)
