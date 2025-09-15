def LeerNumero():
    Numero=float(input("indica el numero que deseas validar: "))
    return Numero

def ValidarNumeroPrimo(Numero):
        if Numero <= 1:
            return "El numero que indicaste no es primo"
        elif Numero == 2:
            return "El numero que indicaste es primo"
        elif Numero % 2 ==0:
            return "El numero que indicaste no es primo"
        else:
            return (f"El numero {Numero} es un numero primo")
            

Numero=LeerNumero()
Validacion= ValidarNumeroPrimo(Numero)
print(Validacion)