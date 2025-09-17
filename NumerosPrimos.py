def EsPrimo(Num):
    
    if Num < 2:
        return False
    for i in range(2,Num):
        if Num % i == 0:
            return False
    return True

Num=2
cont=0
while cont < 101:
    if EsPrimo(Num):
        print(Num)
        cont +=1
    Num +=1 