def calcularMasa(presion, volumen, temperatura):
    resultado = (presion * volumen) / (0.37 * (temperatura + 460))
    return resultado

def mensajeError(msg):
    print("\n >>>", msg)
    input("Presione cualquier letra para continuar.")
    print("")

def leerVehiculos():
    n = int(input("Cantidad de vehiculos? "))
    while n < 1:
        mensajeError("Error. Cantidad de vehiculos inválida")
        n = int(input("Cantidad de vehiculos? "))
    return n

def leerTipoVehiculo():
    tipo = input("Que tipo de vehiculo es: M: Moto || A: Automóvil ")
    while (tipo != "m" and tipo != "M") and (tipo != "A" and tipo != "a"):
         mensajeError("Error. Tipo de vehiculo inválido")
         tipo = input("Que tipo de vehiculo es: M: Moto || A: Automóvil ")
    return tipo 

def leerFloat(msg):
    dato = float(input(msg))
    while dato < 0:
        mensajeError("Error. Valor invádlido")
        dato = float(input(msg))
    return dato

def masaLlantasVehiculo(llantas):
    sumaMasas = 0
    for i in range(1, llantas+1):
        print("\t--> LLanta #", i)
        presion = leerFloat("Presión? ")
        volumen = leerFloat("Volumen? ")
        temperatura = leerFloat("Temperatura? ")
        masa = calcularMasa(presion, volumen, temperatura)
        sumaMasas = sumaMasas + masa

    return sumaMasas


cantLlantas = 0
suma = 0

n = leerVehiculos()
for i in range(n):
    print("\Vehículo #", (i+1))
    print("-----------")

    tipoVeh = leerTipoVehiculo()
    if tipoVeh == "m" or tipoVeh == "M":
        llantas = 2
    else:
        llantas = 4

    cantLlantas = cantLlantas + llantas
    suma = suma + masaLlantasVehiculo(llantas)

promedio = suma / cantLlantas

print("El promedio de la masa de los", n, "Vehiculos es:", promedio)