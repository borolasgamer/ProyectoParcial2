#menu
from Factoriales import factoriales
from Promedio import promedio
from math import factorial

menuprincipal = int(input("Menu Principal: \n 1-Suma de N numeros \n 2-Producto entre N numeros \n 3-Division entre 2 numeros \n 4-calcular el factorial de 1 numero \n 5-Ver tablas de multiplicar \n 6-Calcular el cuadrado y el cubo de 1 numero \n 7-Obtener el promedio de una serie de numeros \n 8-Obtener el valor maximo y minimo de una de una serie de numeros \n 9-Escriba 0 para salir \n"))
if menuprincipal ==1:
    suma=0
    contador=1
    valor = int(input('Ingrese cuantos numeros desea sumar: '))
    while contador <= valor: 
        num = int(input('Ingrese el valor:' ))
        suma+=num
        contador=contador+1
    print("La suma total de los numeros es:", suma)
elif menuprincipal ==2:
    multi=1
    contador=1
    valor = int(input('Ingrese cuantos numeros desea multiplicar: '))
    while contador <= valor: 
        num = int(input('Ingrese el valor:' ))
        multi*=num
        contador=contador+1
    print("El producto total de los numeros es:", multi)
elif menuprincipal ==3:
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    print("La division de", num1, "y", num2, "es:", num1/num2)
elif menuprincipal ==4:
        factoriales()
elif menuprincipal ==5:
            exit=True
            while exit:
                tablas=int(input('Ingresa la tabla que desea visualizar:'))
                if tablas!=1:
                    for f in range(1,11):
                        multiplicacion = tablas * f #hacemos la multiplicación
                        print (tablas,f"x {f} = {multiplicacion}") #mostramos el resultado
                respuesta= input("quieres continuar?:")
                if respuesta == "no":
                    exit=False
                    print('Saliendo de la sección')
                elif respuesta == "si":
                    print("Continuando...")
elif menuprincipal ==6:
            print("Calculo del cuadrado y cubo")
elif menuprincipal ==7:
            promedio()
elif menuprincipal ==8:
            print("Valor maximo y minimo de una lista")
elif menuprincipal ==0:
            print("Saliendo...")
