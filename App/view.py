﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import sys
sys.path.append("DISClib")
from ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar tipo de ordenamiento para el catalogo")
    print("3- Video por categoria y pais")
    print("4- Video tendencia por pais")
    print("5- Video tendencia por categoria")
    print("6- Videos con mas likes")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        t1 = time.process_time()
        print("Cargando información de los archivos ....")
        consulta= int(input("Ingrese 1 para ARRAY_LIST o ingrese 2 para LINKED_LIST: "))
        tipo_de_la_lista = controller.funcion_lista(consulta)
        catalog = controller.initcatalog(tipo_de_la_lista)
        controller.cargarinfocatalogo(catalog)
        print("Se cargaron los videos")
        print("Videos cargados: " + str(lt.size(catalog['videos'])))
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str((t2-t1)*1000) + " milisegundos")

    elif int(inputs[0]) == 2:
        t1 = time.process_time()
        print("Tipos de ordenamientos")
        print("1-Selection Sort")
        print("2-Insertion Sort")
        print("3-Shell Sort")
        print("4-Quick sort")
        print("5-Merge sort")
        tipo = int(input("Seleccione el metodo de ordenamiento que desea ejecutar para el catalogo: "))
        size = int(input("Ingrese el tamaño de la muestra que desea ordenar: "))
        controller.sortVideos(catalog, size, tipo)
        print("Se ordenó el catalogo de acuerdo a la especificación")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str((t2-t1)*1000) + " milisegundos")

    elif int(inputs[0]) == 3:
        t1 = time.process_time()
        pais = input("Ingrese el pais que desea consultar: ")
        categoria = input("Ingrese la categoria que desea consultar: ")
        numero = int(input("Ingrese el numero de videos que desea visualizar:"))
        print("El video con mas dias como tendendia en " + pais + " para la categoria " + categoria + " es:")
        print(controller.videos_categoria_pais(catalog, categoria, pais, numero))
        print("Se ejecutó el requerimiento 3")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 4:
        t1 = time.process_time()
        pais = input("Ingrese el pais que desea consultar: ")
        video = controller.video_trending(catalog,pais)
        nombre = video["title"]
        canal = video["channel_title"]
        dias = video["Dias Tendencia"]
        print(("El titulo del video con mas dias como tendendia en {0} es {1} el nombre del canal es {2} y fue tendencia por {3} dias.").format(pais, nombre, canal, dias))
        print("Se ejecutó el requerimiento 2")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 5:
        t1 = time.process_time()
        categoria = input("Ingrese la categoria que desea consultar: ")
        final = controller.video_categoria(catalog,categoria)
        print("El titulo del video  que mas dias ha sido trending en la categoria {0} (id de la categoria es {1}) fue {2} y su canal fue {3} con el total de {4} dias".format(categoria, final[2],final[0],final[1],final[3]))
        print("Se ejecutó el requerimiento 3")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 6:
        t1 = time.process_time()
        pais = input("Ingrese el pais que desea consultar: ")
        tag = input("Ingrese el tag que desea consultar: ")
        numero = int(input("Ingrese el numero de videos que desea visualizar:"))
        print("Los videos con mas likes para " + pais + " con el tag " + tag + " son:")
        print(controller.videos_likes(catalog, pais, tag, numero))
        print("Se ejecutó el requerimiento 4")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    else:
        sys.exit(0)
sys.exit(0)
