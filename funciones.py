import csv

def extraer_datos_csv(nombre_archivo):
    datos = []

    with open(nombre_archivo, "r", newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            datos.append(fila)


    return datos

def suma(a, b):
    return a + b