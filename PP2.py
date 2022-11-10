##EmilioParte/2-multiplicacionDeNNumeros
# Creamos las listas (vacías al comienzo)
numeros = []
# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = int(input('Ingrese la cantidad de numeros que quiere multiplicar:'))

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ahora podra ingresar el producto", i + 1)
    listanumeros = int(input(": "))
    numeros.append(listanumeros)
    

# Ahora mostremos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", numeros[i])