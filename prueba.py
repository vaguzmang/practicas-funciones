def LeerPrecio():
    precio=float(input("indica el precio del articulo: "))
    return precio


def CalcularDescuento(precio):
    if precio >=150000:
        precio = precio * 0.05
    return precio



ValorIngresado=LeerPrecio()
Descuento=CalcularDescuento(ValorIngresado)
PrecioFinal=ValorIngresado-Descuento


print("-------Descripcion de la Copra------")
print("El valor del articulo es $ ", ValorIngresado)
print(f"El valor del descuento es $ {Descuento:.2f}")
print(f"El valor final del articulo es $ {PrecioFinal:.2f}")

