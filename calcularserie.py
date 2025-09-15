def signo(denominador):
    if denominador % 2 == 0:
        return -1
    else:
        return 1

def mensajeError(msg):
    print("\n>> Error. Valor inválido")
    input("Presione una tecla para continuar")
    print()


def leerN():
    n = int(input("Ingrese el valor de n "))
    while n < 1:
        mensajeError("Valor inválido para n") 
        n = int(input("Ingrese el valor de n "))
    return n

n = leerN()
suma = 0
for i in range(1, n+1):
    suma = suma + signo(i) * (1 / i)

print("El valor de la suma es: ", suma)