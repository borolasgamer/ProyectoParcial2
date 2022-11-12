def factoriales():
    error = False  

    while error == False:
        numfactorial = int (input('Ingrese un numero para calcular su factorial\n'))
        factorial = 1
        if numfactorial <0:
            print ('El factorial para el numero ingresado no existe, por favor ingrese numeros positivos.\n')
        
        if numfactorial ==0:
            factorial = 1
            print ('El factorial para el numero ingresado es: ',factorial)

        if numfactorial >0:
            error = True
            for i in range(1,numfactorial+1):
                factorial= factorial*i
            print ('El factorial del numero ingresado es: ',factorial)