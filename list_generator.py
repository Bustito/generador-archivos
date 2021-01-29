import random
import decimal

# Tipo de datos que se aceptan
tipo_elementos = ['entero', 'real', 'cadena']

columnas = []  # Aca se guardan los datos del archivo a generar

rango = [0, 2]  # Lista utilizada para guardar el rango de las lista random

temp_list = []  # Lista temporal

# Ingreso la cantidad de columnas
col = input("Ingrese la cantidad de columnas: ")
col = int(col)

# Ingreso la cantidad de elementos de la lista
cant = input("Ingrese la cantidad de elementos de la lista: ")
cant = int(cant)

# Por cada columna, se ingresa el nombre de la misma y el tipo de elemento
for i in range(0, col):

    # Tipo de elemento de la columna
    tipo = input(f"\nIngrese el tipo de elementos de la columna {i}: ")
    tipo = str(tipo).lower()

    # Validacion de dato
    while tipo not in tipo_elementos:
        tipo = input("Seleccione un tipo de elemento valido para la columna: ")
        tipo = str(tipo).lower()

    if tipo == 'entero':  # Si es un numero entero
        # Determinar los limites del conjunto
        rango[0] = int(input("Limite inferior del conjunto: "))
        rango[1] = int(input("Limite superior del conjunto: "))

        # Genera la lista de numeros enteros random
        for i in range(0, cant):
            temp_list.append(random.randint(rango[0], rango[1]))

    elif tipo == 'real':  # Si es un numero con coma
        # Determinar los limites del conjunto
        rango[0] = float(input("Limite inferior del conjunto: "))
        rango[1] = float(input("Limite superior del conjunto: "))

        # Genera la lista de numeros real random, con los decimales
        for i in range(0, cant):
            x = round(random.uniform(rango[0], rango[1]), 2)
            temp_list.append(x)

    elif tipo == 'cadena':  # Entonces es una cadena/caracter
        # Determinar la cantidad de valores posibles
        cant_opciones = int(input("Cantidad de opciones: "))

        # Genera la lista previa con el codigo numerico de las cadenas
        for i in range(0, cant):
            temp_list.append(random.randint(0, cant_opciones - 1))

        # Cambia los numeros por su cadena
        for i in range(0, cant_opciones):
            op = input("Ingrese una opcion de cadena: ").lower()
            for a, b in enumerate(temp_list):
                if b == i:
                    temp_list[a] = op

    # Carga la columna de datos
    columnas.append(temp_list.copy())

    # Limpia la lista temporal
    del temp_list[:]

confirmacion = 'N'
# Pide el nombre del archivo a utilizar/generar
msg = '\nIngresar nombre del archivo (con la extension ej: "file.dat"): '
archivo = input(msg).lower()

# Pide la confirmacion del nombre del archivo
while (confirmacion != 'Y'):
    msg = f"Esta seguro que quiere llamar al archivo '{archivo}'? (Y/N): "
    confirmacion = input(msg).upper()

# Abre el archivo
f = open(archivo, mode='w', encoding='utf-8')

# Genera cada fila del archivo y la guarda en este
for i in range(0, cant):
    row = []
    for columna in columnas:
        if columnas.index(columna) == 0:
            row = f"{columna[i]}"
        else:
            row += f"\t{columna[i]}"

    f.write(f"{row}\n")

# FIN