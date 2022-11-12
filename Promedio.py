def promedio():
    num = 0
    contador = 0
    suma = 0

    while num >= 0:
        num = int (input('Ingresa los numeros para calcular el promedio: \n'))
        
        if num > 0:
            contador = contador+1
            suma = suma + num
        
        if num == -1:
            print('El promedio de los numeros ingresados es: ',suma/contador)
