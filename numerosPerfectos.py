import os

os.system("cls")

def encontrar_numeros_perfectos(limite):
  
    print(f"Buscando números perfectos en el rango de 1 a {limite}...")
    
    
    for numero in range(2, limite + 1):
        suma_divisores = 1  
        
        
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                
                suma_divisores += i
        
                if i*i != numero:
                    suma_divisores += numero // i
        
        
        if suma_divisores == numero:
            print(f"Número perfecto encontrado: {numero}")


LIMITE_SUPERIOR = 1000000


encontrar_numeros_perfectos(LIMITE_SUPERIOR)






 