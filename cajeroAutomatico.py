import os

saldo = 100000  
opcion = -1     

while opcion != 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Cajero Automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("0. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Su saldo actual es: ${saldo:,.2f}")
                input("Presione una tecla pra continuar")
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
                if cantidad_deposito > 0:
                    saldo += cantidad_deposito
                    print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:,.2f}")
                else:
                    print("La cantidad a depositar debe ser positiva.")
                input()
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
                if cantidad_retiro > 0:
                    if saldo - cantidad_retiro >= 0: 
                        saldo -= cantidad_retiro
                        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:,.2f}")
                    else:
                        print("Saldo insuficiente. No puede dejar el saldo negativo.")
                else:
                    print("La cantidad a retirar debe ser positiva.")
                input()
            case 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
                input()
            case _: # Opción por defecto para cualquier otro número
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opción no válida. Por favor, seleccione una opción del 0 al 3.")
                input()
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entrada no válida. Por favor, ingrese un número entero.")
        input()