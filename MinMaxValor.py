def min_max():
    print("Ingresa los numeros que quieras, cuando termines escribe 'fin'")
    lista = []
    while True:
        numero = input("Ingresa un numero: ")
        if numero == "fin":
            break
        else:
            lista.append(int(numero))
    print("El numero maximo es: ", max(lista))
    print("El numero minimo es: ", min(lista))
