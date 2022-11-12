#menu

menuprincipal = int(input("Menu Principal: \n 1-Suma de N numeros \n 2-Producto entre N numeros \n 3-Division entre 2 numeros \n 4-calcular el factorial de 1 numero \n 5-Ver tablas de multiplicar \n 6-Calcular el cuadrado y el cubo de 1 numero \n 7-Obtener el promedio de una serie de numeros \n 8-Obtener el valor maximo y minimo de una de una serie de numeros \n 9-Escriba 0 para salir \n"))

if menuprincipal ==1:
            print("suma de numeros")
elif menuprincipal ==2:
            print("multiplicacion de numeros")
elif menuprincipal ==3:
            print("Division de numeros")
elif menuprincipal ==4:
            print("Calculo de un factorial")
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
            print("Obtener el promedio de una serie de numeros")
elif menuprincipal ==8:
            print("Valor maximo y minimo de una lista")
elif menuprincipal ==0:
            print("Saliendo...")
