#Calculo cuadrado y cubo 
from math import sqrt
def Calculo2y3():
    while True:
        try:
            limite_inferior = int(input('Digite el valor para el límite inferior del rango: '))

            break
        except ValueError:
            print('ERROR: Debe digitar un número entero.')
        print()
    print()

    while True:
        try:
            limite_superior = int(input('Digite el valor para el límite superior del rango: '))

            if limite_superior <= limite_inferior:
                print('ADVERTENCIA: El límite superior debe ser mayor al límite inferior.')
                print()
                continue

            break
        except ValueError:
            print('ERROR: Debe digitar un número entero.')
        
        print()

    print()

    numeros = list(range(limite_inferior, limite_superior + 1))

    for n in numeros:
        print(n**2, n**3, 2)