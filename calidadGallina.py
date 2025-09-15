def mensajeError(msg):
    print("\n >>>", msg)
    input("Presione cualquier letra para continuar.")
    print("")

def leerCantidadGallinas():
    n = int(input("¿Cantidad de gallinas? "))
    while n < 1:
        mensajeError("Error. Cantidad de gallinas inválida")
        n = int(input("¿Cantidad de gallinas? "))
    return n

def leerFloat(msg):
    dato = float(input(msg))
    while dato <= 0:
        mensajeError("Error. Valor inválido")
        dato = float(input(msg))
    return dato

def calidadGallina(numGallina):
    print("\nGallina #", numGallina + 1)
    peso = leerFloat("Peso de la gallina? ")
    altura = leerFloat("Altura de la gallina? ")
    huevos = leerFloat("Número de huevos que pone? ")
    calidad = (peso * altura) / huevos
    return calidad

def calcularPrecio(promedio):
    if promedio >= 15:
        precio = 1.2 * promedio
    elif promedio > 8:
        precio = 1.0 * promedio
    else:
        precio = 0.8 * promedio
    return precio

n = leerCantidadGallinas()
suma = 0
for i in range(n):
    suma = suma + calidadGallina(i)

promedio = suma / n
precio = calcularPrecio(promedio)
print("El precio del huevo es:", precio)