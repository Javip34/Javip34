
import csv
import os

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
    with open(path, newline='', encoding='utf-8') as File: #abrir  archivo
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
    return arr_keys


def output_file(arr, title): #crea un archivo de texto donde se guardan las llaves
    file = open(title, "w")
    for i in arr: #itera en el arreglo e guarda en cada fila del archivo la llave correspondiente
        file.write(str(i) + os.linesep)
    print("archivo generado")
    file.close() #cierra el archivo



arr = abrir(año=2020) #obtener  las llaves del archivo CSV de accidentes de transito
output_file(arr, title= "llaves_Accidentes.txt") #genera archivo de salida con las llaves
arr2 = read_dataset(dataset2_path) #obtener las llaves del archivo CSV de las id  de vídeos de yotutube
output_file(arr2, title="llaves_Videos.txt") #genera archivo de salida con las llaves