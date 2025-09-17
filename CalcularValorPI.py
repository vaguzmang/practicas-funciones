

def calcularPi(interaciones):
    interaciones=1000000
    pi=0
    for i in range(interaciones):
        pi += ((-1)** i) / (2 *i + 1)

    pi *= 4
    print(f"El valor aproximado de pi con 8 decimales es : {pi:.8f}")


calcularPi(1000000)


