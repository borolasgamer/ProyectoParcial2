#menu
class MenuPrincipal:
    menuprincipal = int(input("Menu Principal: \n 1-Suma de N numeros \n 2-Producto entre N numeros \n 3-Division entre 2 numeros \n 4-calcular el factorial de 1 numero \n 5-Ver tablas de multiplicar \n 6-Calcular el cuadrado y el cubo de 1 numero \n 7-Obtener el promedio de una serie de numeros \n 8-Obtener el valor maximo y minimo de una de una serie de numeros \n 9-Escriba 0 para salir \n"))
    while menuprincipal !=0:
        if menuprincipal ==1:
            print("suma de numeros")
        elif menuprincipal ==2:
            print("multiplicacion de numeros")
        elif menuprincipal ==3:
            print("Division de numeros")
        elif menuprincipal ==4:
            print("Calculo de un factorial")
        elif menuprincipal ==5:
            tabla=int(input("seleccione una de las tablas de multiplicar:"))
