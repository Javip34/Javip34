import math
import csv
import math

import numpy as np
import pandas
import matplotlib.pyplot as plt
from random import shuffle
import json
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


def conversor_decimal(n): #convierte una cadena de numeros binarios a notación decimal
    sumador = 0
    multiplicador = 1
    for s in n:
        if s == 1:
            sumador  = sumador + multiplicador
        multiplicador = multiplicador * 2
    return sumador


def binario(num, P): #obtiene lo P binarios más significativos de un entero
    binario = []
    cont = 0
    while num != 0:
        binario.insert(0, num % 2)
        num = num // 2
        cont += 1
    indice = conversor_decimal(binario[0:P])
    return  indice

def abrir(año): # abrir archivo de caso de accidentes automovilisticos
    with open('atus_00_valor_muertos.csv', encoding='utf8') as csvfile:
        r = csv.DictReader(csvfile)
        arr = []
        for i in r:
            if int(i['cve_municipio']) != 0 and int(i['int']) != 0 and int(i['año']) == año:
                caso = i['id_indicador'] + '00000'
                estado = i['int'] + '000'
                if int(caso) + int(estado) + int(i['cve_municipio']) not in arr:
                    arr.append(int(caso) + int(estado) + int(i['cve_municipio']))
    return arr



def generar_tabla(rango): # genera tabla hashing vacía
    return [[] for _ in range(rango)]

def dividirllaves(arr): #obten dos listas de llaves a partir de la lista original
    usadas = arr[0:int(len(arr) * .8)]
    no_usadas = arr[int(len(arr) * .8) : len(arr) - 1]
    return usadas, no_usadas


def hashing_división(arr, rango):
    b = len(arr)
    new = generar_tabla(rango)
    indices = []
    for s in arr:
        index = int(int(s) % rango)
        new[index].append(s)
        indices.append(index)
    return new, indices


def hashing_multiplicacion(arr, w, r, variaA): #realiza hashing por método de multiplicación
    A = variaA*int(2 ** w * ((math.sqrt(5) - 1) / 2))
    rango = 2 ** r
    new = generar_tabla( rango)
    indices = []
    for s in arr:
        num = A * s % 2 ** 64
        index = binario(num, r)
        new[index].append(s)
        indices.append(index)
#        cont = 0
#        num = A * cont + s % 2 ** w
#        index = binario(num, r)
#        if index in indices:
#            while index in indices:
#                num = A * cont + s % 2 ** w
#                index = binario(num, r)
#                cont += 1
#            new[index].append(s)
#            indices.append(index)
#        else:
#            new[index].append(s)
#            indices.append(index)
    return new, indices


def genera_histograma(arr, title, color): #crea el histograma
    plt.hist(arr, 10, color=str(color), ec='black')
    plt.title(str(title))
    plt.show()





def busquedas_p5(arr, hash, type, w, r, variaA, color):
    #r es el valor de m
    buscar = arr
    if type == 'multiplicación':
        A = variaA * int(2 ** w * ((math.sqrt(5) - 1) / 2))
        pasos = []
        for i in buscar:
            cont = 0
           # cont = 1
           # sw = False
           # while sw != True and cont <= len(arr):
            num = A * i % 2 ** w
            index = binario(num, r)
           #     print(index, cont)
           #     if len(hash[index]) != 0 and hash[index][0] == i:
           #         print("ok")
           #         sw = True
           #     else:
           #         cont += 1
            for n in hash[index]:
                if n == i:
                    break
                cont += 1
            pasos.append(cont)
        ejex = []
        for k in range(len(buscar)):
            ejex.append(k + 1)
        promedio = sum(pasos) / len(pasos)
        plt.plot(ejex, pasos, marker = 'o', color = color, label = 'busquedas')
        plt.axhline(promedio, label = 'promedio de busquedas')
        plt.legend(loc = 'upper right')
        plt.xlabel("Número de elementos buscados")
        plt.ylabel("Pasos hasta encontrar elemento")
        lab = 'busqueda' + str(variaA) + 'x A con m = 2^' + str(r)
        plt.title(lab)
        plt.grid(axis='y', color='black', linestyle='dashed')
        plt.show()
    if type == 'División':
        pasos = []
        for i in buscar:
            index = i % r
            cont = 0
            for n in hash[index]:
                if i == n:
                    break
                cont += 1
            pasos.append(cont)
        ejex = []
        for k in range(len(buscar)):
            ejex.append(k + 1)
        promedio = sum(pasos) / len(pasos)
        plt.plot(ejex, pasos, marker='o', color=color, label='busquedas')
        plt.axhline(promedio, label='promedio de busquedas')
        plt.legend(loc='upper right')
        plt.xlabel("Número de elementos buscados")
        plt.ylabel("Pasos hasta encontrar elemento")
        lab = 'busqueda' + str(variaA) + 'x A con m = 2^' + str(r)
        plt.title(lab)
        plt.grid(axis='y', color='black', linestyle='dashed')
        plt.show()




def insericon_p6(arr, hash, type, w, r, variaA, color):
    buscar = arr
    if type == 'multiplicación':
        A = variaA * int(2 ** w * ((math.sqrt(5) - 1) / 2))
        pasos = []
        for i in buscar:
            num = A * i % 2 ** w
            index = binario(num, r)
            cont = 0
            if len(hash[index]) == 0:
                hash[index].insert(0,i)
                cont += 1
            else:
                cont += len(hash[index])
                hash[index].insert(0,i)
            pasos.append(cont)
        ejex = []
        for k in range(len(buscar)):
            ejex.append(k + 1)
        promedio = sum(pasos) / len(pasos)
        print(promedio)
        plt.plot(ejex, pasos, marker='o', color=color, label='inserciones')
        plt.axhline(promedio, label='promedio de inserciones')
        plt.legend(loc='upper right')
        plt.xlabel("Número de elementos insertados")
        plt.ylabel("Pasos para insertar elemento")
        lab = 'inserción' + str(variaA) + 'x A con m = 2^' + str(r)
        plt.title(lab)
        plt.grid(axis='y', color='black', linestyle='dashed')
        plt.show()
    if type == 'División':
        pasos = []
        for  i in buscar:
            cont  = 0
            index = i % r
            if len(hash[index]) == 0:
                hash[index].insert(0, i)
                cont += 1
            else:
                cont += len(hash[index])
                hash[index].insert(0, i)
            pasos.append(cont)
        ejex = []
        for k in range(len(buscar)):
            ejex.append(k + 1)
        promedio = sum(pasos) / len(pasos)
        print(promedio)
        plt.plot(ejex, pasos, marker='o', color=color, label='inserciones')
        plt.axhline(promedio, label='promedio de inserciones')
        plt.legend(loc='upper right')
        plt.xlabel("Número de elementos insertados")
        plt.ylabel("Pasos para insertar elemento")
        lab = 'inserción' + str(variaA) + 'x A con m = 2^' + str(r)
        plt.title(lab)
        plt.grid(axis='y', color='black', linestyle='dashed')
        plt.show()




def  eliminación_p7(arr, hash, type, w, r, variaA, color):
    buscar = arr
    if type == 'multiplicación':
        A = variaA * int(2 ** w * ((math.sqrt(5) - 1) / 2))
        pasos = []
        for i in buscar:
            num = A * i % 2 ** w
            index = binario(num, r)
            cont = 0
            for n in hash[index]:
                if n == i:
                    hash[index].remove(n)
                    break
                cont += 1
            pasos.append(cont)
        ejex = []
        for k in range(len(buscar)):
            ejex.append(k + 1)
        promedio = sum(pasos) / len(pasos)
        plt.plot(ejex, pasos, marker='o', color=color, label='busquedas')
        plt.axhline(promedio, label='promedio de busquedas')
        plt.legend(loc='upper right')
        plt.xlabel("Número de elementos eliminados")
        plt.ylabel("Pasos hasta encontrar elemento a eliminar y eliminarlo")
        lab = 'eliminación' + str(variaA) + 'x A con m = 2^' + str(r)
        plt.title(lab)
        plt.grid(axis='y', color='black', linestyle='dashed')
        plt.show()
    if type == 'Disvisión':
        pasos = []
        cont = 0
        for i in buscar:
            index = i % r
            for  n in hash[index]:
                if n == i:
                    hash[index].remove(n)
                    break
                cont += 1
            pasos.append(cont)
        ejex = []
        for k in range(len(buscar)):
            ejex.append(k + 1)
        promedio = sum(pasos) / len(pasos)
        plt.plot(ejex, pasos, marker='o', color=color, label='busquedas')
        plt.axhline(promedio, label='promedio de busquedas')
        plt.legend(loc='upper right')
        plt.xlabel("Número de elementos eliminados")
        plt.ylabel("Pasos hasta encontrar elemento a eliminar y eliminarlo")
        lab = 'eliminación' + str(variaA) + 'x A con m = 2^' + str(r)
        plt.title(lab)
        plt.grid(axis='y', color='black', linestyle='dashed')
        plt.show()





def frecuencias(arr, indices,title):
    cantidades = []
    plt.hist(indices, 200, color='blue', ec='black') #genera el histograma de la distribución de llaves
    plt.title(title)
    plt.show()
    for i in arr:
        cantidades.append(len(i))
    plt.hist(cantidades, 200, color='blue', ec='black') #genera el histograma de la cantidad de elementos por slot
    plt.title(title)
    plt.show()
    axis_x = np.arange(1, len(cantidades) + 1) #genera gráfica de la distribución real de la tabla hash
    fig, ax = plt.subplots()
    ax.bar(axis_x, cantidades)
    newtitle = "Otro" + title
    ax.set_title(newtitle)
    ax.set_ylabel("Frecuencias")
    ax.set_xlabel("Claves")
    plt.show()

arr = abrir(año= 2020)
lis = []
for k in arr:
    b = int(k % 2**31)
    #b = b // 2**23
    lis.append(b)
w = 64
usadas, nousadas = dividirllaves(lis)
nousadas7 = nousadas[0:len(nousadas) // 2]
tablashash = []
indiceshash = []
shuffle(usadas)
buscar = usadas[0: int(len(arr) * .2)]
m = [12,13,14]
A = [1,2,3]
color = ['blue', 'brown', 'green']
for i in A: #experimentos con hash de multiplicación
    cont = 0
    for s in m:
        new, indices = hashing_multiplicacion(usadas, w, s, i)
        type = 'multiplicación'
        frecuencias(new,indices,  title = "Histograma de llaves con A = A* "+ str(i) + " y M = 2^" + str(s))
        busquedas_p5(buscar, new, type, w, s, i, color[cont])
        insericon_p6(nousadas, new, type, w, s, i, color[cont])
        eliminación_p7(nousadas7, new, type, w, s, i, color[cont])
        cont += 1


M = [787,859,1152]
cont = 0
i = 0
for n in M: # experimentos  con hash de división
    new, indices = hashing_división(usadas, n)
    type = 'División'
    frecuencias(new, indices, title= "Histograma de llaves con M=" + str(787))
    busquedas_p5(buscar, new, type, w, n, i, color[cont])
    insericon_p6(nousadas, new, type, w, n, i, color[cont])
    eliminación_p7(nousadas7, new, type, w, n, i, color[cont])
    cont += 1





