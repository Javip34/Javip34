#Creado por Javier Alberto Pulido Solis
#Código de pruebas para funciones hash de multiplicación
#Solo nececita correr  el script, los casos de prueba ya vienen  definidos como las m a usar las A a usar
#asegurarse que cuando corra el sript se tenga el archivo CSV en la misma carpeta de la que está corriendo el script
#el código genera una serie de gráficas correspondientes a  todos los puntos de la tarea, estas gráficas son para la base de datos de accidentes automovilisticos

import csv
import math
import os
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

dataset2_path = 'CAvideos.csv'
total_records = 2000
def string_to_numbers(key):
    """Get a alphanumeric string and convert it to a number"""

    numeric_key = ""

    for d in key:
        numeric_key += str(ord(d))  # Use ascii code to convert each character

    return numeric_key

def read_dataset(path):
    """It receives a path from a dataset and reads it. Then get 2000 alphanumeric keys and return them as a number each"""

    arr_keys = []

    with open(path, newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        num_rows = -1

        for row in reader:
            num_rows += 1

            if num_rows == 0:  # If the record is just the column name, then it will ignore it
                continue

            numeric_key = string_to_numbers(row[0])  # Change the alphanumeric key to a number

            arr_keys.append(numeric_key)

            if num_rows >= total_records:  # Stop reading the dataset because 2000 records were obtained
                break

        print("closed")
    print(len(arr_keys))
    return arr_keys




def abrir(año): # abrir archivo de caso de accidentes automovilisticos
    with open('atus_00_valor_muertos.csv', encoding='utf8') as csvfile: #abre el archivo del que obtengo los datos
        r = csv.DictReader(csvfile) #guarda los datos en una variable r
        arr = []
        for i in r: #obtener los datos almacenados
            if int(i['cve_municipio']) != 0 and int(i['int']) != 0 and int(i['año']) == año: #obtener las llaves del archivo CSV con la id del municipio, estado y casos
                caso = i['id_indicador'] + '00000' #incrementar espacios  del indicador de caso para concatenar con los demás id
                estado = i['int'] + '000' #incrementar espacios de la id de estado para concatenarlo con el municipio
                if int(caso) + int(estado) + int(i['cve_municipio']) not in arr:
                    arr.append(int(caso) + int(estado) + int(i['cve_municipio'])) #agregar llaves generadas
    return arr #retornar llaves generadas



def generar_tabla(rango): # genera tabla hash vacía para insertar los elementos
    return [[] for _ in range(rango)]

def dividirllaves(arr): #obten dos listas de llaves a partir de la lista original
    usadas = arr[0:int(len(arr) * .8)] #obtener  una  fraccion del 80 %
    no_usadas = arr[int(len(arr) * .8) : len(arr) - 1] #obtener un fraccion del 20 %
    return usadas, no_usadas #retornar listas para los  experimentos



def hashing_multiplicacion(arr, w, r, variaA): #realiza hashing por método de multiplicación
    if variaA == 1: #activa primera A
        A = variaA*int(2 ** w * ((math.sqrt(5) - 1) / 2)) #valor de A1
    elif variaA == 2: #activa segunda A
        A = 2 ** w * .5864 #valor de A2
    elif variaA == 3: #activa tercera A
        A = 2 ** w * math.sqrt(5) / 3 #valor de A3
    elif variaA == 4:
        print("Aqui va un valor de A para los videos ")
    elif variaA == 5:
        print("aqui va un valor de A para lo videos ")
    elif variaA == 6:
        print("aqui va un valor de A para los videos ")
    rango = 2 ** r #determina el tamaño de la tabla hash M
    new = generar_tabla( rango) #generar tabla hash vacía
    indices = []
    for s in arr: #iterar en las llaves
        temp = bin((int(A) * int(s)) % 2 ** w)[2:] #obtener la cadena binaria equivalente y determinar su modulo por 2 ** w
        for _ in range(w - r): #agrega los 0 faltantes para que la palabra esté del tamaño de w
            temp[::-1] + str(0)
        index = int(temp) % 2 ** r #obtener los b bits mas significativos de la segunda mitad
        new[index].append(s) #indexar K en en indice "index" dentro de la tabla hash
        indices.append(index) #guardar el indice en una lista para graficar
    return new, indices


def busquedas_p5(arr, hash, w, r, variaA): #realiza gráficas del problema 5 para experimentos de accidentes de tráfico
    buscar = arr.copy()
    if variaA == 1:  # define  los valores de A seleccionados
        A = variaA * int(2 ** w * ((math.sqrt(5) - 1) / 2))
    if variaA == 2:
        A = 2 ** w * .5864
    if variaA == 3:
        A = 2 ** w * math.sqrt(5) / 3
    elif variaA == 4:
        print("Aqui va un valor de A para los videos ")
    elif variaA == 5:
        print("aqui va un valor de A para lo videos ")
    elif variaA == 6:
        print("aqui va un valor de A para los videos ")
    pasos = []
    for i in buscar:  # iterare en la lista de llaves que deseamos buscar en la tabla hash
        cont = 0
        temp = bin((int(A) * int(i)) % 2 ** w)[2:]
        for _ in range(w - r):
            temp[::-1] + str(0)
        index = int(temp) % 2 ** r  # asignamos un indice a la llave para buscar en la tabla hash
        for n in hash[index]:  # recorremos el slot y contamos las comparaciones hasta que K sea encontrada
            cont += 1
            if n == i:
                break
        pasos.append(cont)  # recopilamos la cantidad de comparaciones para encontrar K
    lab = 'busqueda' + str(variaA) + 'x A con m = 2^' + str(r)  # titulo de la gráfica
    ejex = []
    for k in range(len(buscar)):  # creamos  nuestro eje x para la gráfica
        ejex.append(k + 1)
    promedio = sum(pasos) / len(pasos)  # determinamos el promedio de pasos para busqueda
    fig, ax = plt.subplots()  # incializamos grafica
    ax.bar(ejex, pasos)  # definimos nuestor ejex y y con los valores obtenidos
    ax.axhline(promedio, label='Promedio de busqueda' + str(promedio),
               color='red')  # imprimimos el promedio de pasos como una linea roja sobre la gráfica
    ax.legend(loc='upper right')
    ax.set_title(lab)  # inicializamo el titulo de la gráfica
    ax.set_ylabel("Frecuencias")  # nombramos nuestros ejes
    ax.set_xlabel("Claves")
    plt.show()  # lanzamos gráfica




def insericon_p6(arr, hash, w, r, variaA): #realiza las gráficas del problema 5 para casos de inserción a la tabla hash
    buscar = arr.copy()
    pasos = []
    if variaA == 1:  # define  los valores de A seleccionados
        A = variaA * int(2 ** w * ((math.sqrt(5) - 1) / 2))
    if variaA == 2:
        A = 2 ** w * .5864
    if variaA == 3:
        A = 2 ** w * math.sqrt(5) / 3
    elif variaA == 4:
        print("Aqui va un valor de A para los videos ")
    elif variaA == 5:
        print("aqui va un valor de A para lo videos ")
    elif variaA == 6:
        print("aqui va un valor de A para los videos ")
    for i in buscar:  # buscamos en la lista de k que deseamos insertar
        temp = bin((int(A) * int(i)) % 2 ** w)[2:]  # detemrinamos el indice que le corresponde  a la llave
        for _ in range(w - r):
            temp[::-1] + str(0)
        index = int(temp) % 2 ** r
        cont = 0
        if len(hash[index]) == 0:  # su la celda de la tabla hash está vacía insertar el elemento (no hay colisión)
            hash[index].insert(0, i)
            cont += 1
        else:  # si no está vacía  recorrer la lista hasta el último lugar y insertar elemento que ha colisionaod (hoy colisión)
            cont += len(hash[index])
            hash[index].insert(0, i)
        pasos.append(cont)  # recopilamos los pasos efectuados para insertar cada eleemnto en la lista "buscar"
    ejex = []
    for k in range(len(buscar)):  # generamos nuestro eje x para la gráfica
        ejex.append(k + 1)
    promedio = sum(pasos) / len(pasos)  # detemrinamos el promedio de pasos
    lab = 'Inserción de elementos' + str(variaA) + 'x A con m = 2^' + str(r)  # nombre de la tabla y graficamos los  resultados
    fig, ax = plt.subplots()
    ax.bar(ejex, pasos)
    ax.axhline(promedio, label='Promedio de inserción' + str(promedio), color='red')
    ax.legend(loc='upper right')
    ax.set_title(lab)
    ax.set_ylabel("Frecuencias")
    ax.set_xlabel("Claves")
    plt.show()




def  eliminación_p7(arr, hash, w, r, variaA): #realiza las graficas del problema 7 para casos de suprecion en la tabla hash
    buscar = arr.copy()
    if variaA == 1:  # define  los valores de A seleccionados
        A = variaA * int(2 ** w * ((math.sqrt(5) - 1) / 2))
    if variaA == 2:
        A = 2 ** w * .5864
    if variaA == 3:
        A = 2 ** w * math.sqrt(5) / 3
    elif variaA == 4:
        print("Aqui va un valor de A para los videos ")
    elif variaA == 5:
        print("aqui va un valor de A para lo videos ")
    elif variaA == 6:
        print("aqui va un valor de A para los videos ")
    pasos = []
    for i in buscar:
        temp = bin((int(A) * int(i)) % 2 ** w)[2:]
        for _ in range(w - r):
            temp[::-1] + str(0)
        index = int(temp) % 2 ** r
        cont = 0
        for n in hash[index]:
            cont += 1
            if n == i:
                hash[index].remove(n)
                break
        pasos.append(cont)
    ejex = []
    for k in range(len(buscar)):
        ejex.append(k + 1)
    promedio = sum(pasos) / len(pasos)
    lab = 'Eliminación de elementos' + str(variaA) + 'x A con m = 2^' + str(r)
    fig, ax = plt.subplots()
    ax.bar(ejex, pasos)
    ax.axhline(promedio, label='Promedio de eliminación' + str(promedio), color='red')
    ax.legend(loc='upper right')
    ax.set_title(lab)
    ax.set_ylabel("Frecuencias")
    ax.set_xlabel("Claves")
    plt.show()


def frecuencias(arr, indices,color , title): # función que calcula las gráficas de la parte 4 de la tarea
    cantidades = []
    plt.hist(indices, 200, color=color, ec='black') #genera el histograma de la distribución de llaves
    plt.title(title) #incializamos el titulo
    plt.show() #mostramos  gráfica
    for i in arr: #recorremos tabla hash
        cantidades.append(len(i)) #contamos cuantos elementos tiene cada slot y los guardamos en una  lista
    plt.hist(cantidades, 10, color=color, ec='black') #genera el histograma de la cantidad de elementos por slot
    plt.ylabel("frecuencia de elementos en slot")
    plt.xlabel("Cantidad de elementos por slot")
    plt.title("Histograma de cantidad de elementos por Slot")
    plt.show() #mostramos histograma
    axis_x = np.arange(1, len(cantidades) + 1) #genera gráfica de la distribución real de la tabla hash
    fig, ax = plt.subplots()
    ax.bar(axis_x, cantidades) #definimos nuestros ejes x y y
    newtitle = "Distribución real de tabla Hash" + title #bombre de la tabla
    ax.set_title(newtitle)
    ax.set_ylabel("Elementos")
    ax.set_xlabel("Claves")
    plt.show() #mostramos tabla



def main_multiplicacion_Atomovilisticos(): #corre los experimentos de los accidentes automovilisticos con método de multipliciación
    print("Has ejecutado los experimentos de Hashing de multiplicación para las llaves de los accidentes automovilisticos")
    arr = abrir(año=2020)  # Llamamos función de accidentes para recoopilar las llaves de todos los accidentes en  el año 2020
    w = 28  # definimos el valor w de longitud de palabra con el que vamos a trabajar dada lanaturaleza de las llaves generadas
    plt.hist(arr, 200, color='black')  # inciamos  histograma de mapeo de frecuencias de llaves
    plt.title("Histograma de frecencia de llaves generadas del archivo CSV")  # titulo de la tabla
    plt.ylabel("frecuencia")
    plt.xlabel("llaves CSV mapeadas 1 a 1")
    plt.show()  # mostramos histograma
    print(len(arr))
    usadas, nousadas = dividirllaves(arr)  # llamamos a nuestra funcion que divide las llaves en una 80% y 20%
    nousadas7 = nousadas[0:len(nousadas) // 2]  # dividmos las llaves correspondientes al 20% a la mitad
    shuffle(usadas)  # barajeamos las llabes usadas
    buscar = usadas[0: int(len(arr) * .2)]  # tomamos el 20% de las llaves usadas aleatorias
    m = [11, 12, 13]  # definomos nuestros exponentes de m  --> 2 ^ (m)
    A = [1, 2, 3]  # definimos  conmutadora de valores  de A
    color = ['blue', 'brown', 'green']  # colores para la gráfica
    cont = 0
    for i in A:  # experimentos con hash de multiplicación para accidentes automovilisticos
        for s in m:
            new, indices = hashing_multiplicacion(usadas, w, s,i)  # llamamos a nuestra función encargada de crear tabla hash
            frecuencias(new, indices, color[cont],title="Histograma de llaves con A = A* " + str(i) + " y M = 2^" + str(s))  # llamamos a la funcion para graficar las frecuencias
            busquedas_p5(buscar, new, w, s,i)  # llamamos a la funcion para ejecutar el experimento de busquedas en tabla hash
            insericon_p6(nousadas, new, w, s,i)  # llamamos la funcion para ejecutar los experimentos de insercion en tabla hash
            eliminación_p7(nousadas7, new, w, s,  i)  # llamamos la funcion para ejecutar las supresiones en la talba hash
        cont += 1


def main_multiplicaicon_Videos(): #corre todos los experimentos de los Videos para el método de  multiplicación
    print("Has ejecutado los experimentos de Hashing de multiplicación para las llaves de los Videos ")
    arr = read_dataset(dataset2_path)
    w = 28
    plt.hist(arr, 200, color='black')  # inciamos  histograma de mapeo de frecuencias de llaves
    plt.title("Histograma de frecencia de llaves generadas del archivo CSV")  # titulo de la tabla
    plt.ylabel("frecuencia")
    plt.xlabel("llaves CSV mapeadas 1 a 1")
    plt.show()  # mostramos histograma
    print(len(arr))
    usadas, nousadas = dividirllaves(arr)  # llamamos a nuestra funcion que divide las llaves en una 80% y 20%
    nousadas7 = nousadas[0:len(nousadas) // 2]  # dividmos las llaves correspondientes al 20% a la mitad
    shuffle(usadas)  # barajeamos las llabes usadas
    buscar = usadas[0: int(len(arr) * .2)]  # tomamos el 20% de las llaves usadas aleatorias
    m = [11, 12, 13]  # definomos nuestros exponentes de m  --> 2 ^ (m)
    A = [1, 2, 3]  # definimos  conmutadora de valores  de A --> estos solo sirven para cambiar de valores de A
    color = ['yellow', 'black', 'purple']  # colores para la gráfica
    cont = 0
    for i in A:  # experimentos con hash de multiplicación para Vídeos
        for s in m:
            new, indices = hashing_multiplicacion(usadas, w, s,i)  # llamamos a nuestra función encargada de crear tabla hash
            frecuencias(new, indices, color[cont],title="Histograma de llaves con A = A* " + str(i) + " y M = 2^" + str(s))  # llamamos a la funcion para graficar las frecuencias
            busquedas_p5(buscar, new, w, s,i)  # llamamos a la funcion para ejecutar el experimento de busquedas en tabla hash
            insericon_p6(nousadas, new, w, s,i)  # llamamos la funcion para ejecutar los experimentos de insercion en tabla hash
            eliminación_p7(nousadas7, new, w, s,i)  # llamamos la funcion para ejecutar las supresiones en la talba hash
        cont += 1




main_multiplicacion_Atomovilisticos() #correr experimentos de los Accidentes por método de multiplicación
#main_multiplicaicon_Videos() #correr experimentos de los videos



