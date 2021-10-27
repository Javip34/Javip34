- 👋 Hi, I’m @Javip34
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Javip34/Javip34 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
import csv
import math
import pandas
import matplotlib.pyplot as plt
import json
import  numpy as np


def cubetas(): #genera cubeta
    cubito =[]
    for i in range(0,10):
        cubito.append([])
    return cubito

def k(P): #determinna el valor de k
    valor = 0
    for s in P:
        valor = max(valor, s)
    return len(str(valor))

def Radix(arr,iterar):
    for s in range(iterar):
        cubitos = cubetas()
        for i in range(len(arr)):
            indice = arr[i] // 10 ** (s) % 10
            cubitos[indice].append(arr[i])
        arr = []
        for k in cubitos:
            if len(k) != 0:
                for t in k:
                    arr.append(t)
    return arr


def abrir(año):
    with open('atus_00_valor_muertos.csv', encoding='utf8') as csvfile:
        r = csv.DictReader(csvfile)
        print(r)
        arr = []
        for i in r:
            if int(i['cve_municipio']) != 0 and int(i['int']) != 0 and int(i['año']) == año:
                caso = i['id_indicador'] + '00000'
                estado = i['int'] + '000'
                if int(caso) + int(estado) + int(i['cve_municipio']) not in arr:
                    arr.append(int(caso) + int(estado) + int(i['cve_municipio']))
    return arr







#########################################################################
def conversor_decimal(n): #convierte una cadena de numeros binarios a notación decimal
    sumador = 0
    multiplicador = 1
    for s in n:
        if s == 1:
            sumador  = sumador + multiplicador
        multiplicador = multiplicador * 2
    return sumador


def binario(num, P, w):
    binario = []
    cont = 0
    while num != 0:
        binario.insert(0, num % 2)
        num = num // 2
    for _ in range(w- P):
        binario[::-1].append(0)
    indice = conversor_decimal(binario[0:P])
    return  indice
########################################################################
def generar_tabla(rango):
    return [[] for _ in range(rango)]

def hashing_división(arr, rango):
    new = generar_tabla(rango)
    indices = []
    for s in arr:
        index = int(int(s) % rango)
        new[index].append(s)
        indices.append(index)
    return new, indices


def Multiplicacion(k,r, w, A):
    #A = 2 ** w * (math.sqrt(5) -1) / 2
    #A= 2 ** w * .5864
    #A = 2 ** w * math.sqrt(5)/3
    mod = bin((int(A) * int(k)) % 2 ** w)[2:]
    for _ in range(w-r):
        mod[::-1] + str(0)
    index = int(int(mod) % 2 ** r)
    return index

def hashing2(arr, p, A, w):
    print("input", len(arr))
    rango = 2 ** p
    new = generar_tabla(rango)
    indices = []
    for s in arr:
        index = Multiplicacion(s, p, w, A)
        new[index].append(s)
        indices.append(index)

    print("indeces", len(indices))
    return new, indices

def dividirllaves(arr): #obten dos listas de llaves a partir de la lista original
    usadas = arr[0:int(len(arr) * .8)]
    no_usadas = arr[int(len(arr) * .8) : len(arr) - 1]
    return usadas, no_usadas

#1409
#1423
#1427
#1429
#1433
#1439
#1447
#1451



arr = abrir(año = 2020)
print("logitud de elementos", len(arr))
usados, no = dividirllaves(arr)
#www = []
#for nw in range(0, len(usados)):
#    www.append(nw)
#new, inde = hashing2(usados) #new es la tabla hash con los llaves insertadas y inde son lo indices que se generaron de la función hash (solo para graficar)

lis = []
for k in usados:
    b = int(k % 2**31)
    #b = b // 2**23
  #  print(b)
    lis.append(b)


A = [134517788,
]
p = 11
for  i in A:
    new, inde = hashing2(usados, p, i,w=28)
    cantidades = []
    cont = 0
    for ii in new:  ########################################################obtener distribución de las llaves en la tabla hash
        print(ii)
        cont += len(ii)
        cantidades.append(len(ii))
    plt.hist(cantidades, 20, color='blue', ec='black')
    plt.title('histograma de espacios por slot' + str(i))
    plt.show()
    plt.hist(inde, 200, color='blue', ec='black')
    plt.title('histograma de espacios por slot')
    plt.show()
