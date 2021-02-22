"""
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
sys.path.append("DISClib")
import controller
import model
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def tipo_de_lista():
    lista=int(input("ingrese 1 para array_list o ingrese 2 para linked_list: "))
    centinela=True
    while centinela:
        if lista == 1 or lista == 2:
            break
        elif lista == 0:
            break
        else:
            print("si desea salir ingrese 0")
            lista=int(input("ingrese 1 para array_list o ingrese 2 para linked_list"))
    return lista 

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Video por categoria y pais")
    print("3- Video tendencia por pais")
    print("4- Video tendencia por categoria")
    print("5- Videos con mas likes")

catalog = None

"""
Menu principal
"""
tipo_lista= int(tipo_de_lista())
while True:
    
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        if tipo_lista == 1 or tipo_lista == 2:
            t1 = time.process_time()
            print("Cargando información de los archivos ....")
            catalog = controller.initcatalog(tipo_lista)
            controller.cargardatos(catalog)
            print("Se cargaron los videos")
            print("Videos cargados: " + str(lt.size(catalog['videos'])))
            t2 = time.process_time()
            print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")       
    elif int(inputs[0]) == 2:
        t1 = time.process_time()
        function= input("¿por que metodo de ordanamiento desea hacer?\nselectionsort,insertionsort o shellsort")
        
        comparacion=input("si desea hacerlo de mayor a menor seleccione b de lo contrario seleccione a")
        model.ordenar(function,catalog,comparacion)
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 3:
        t1 = time.process_time()
        print("Se ejecutó el requerimiento 2")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 4:
        t1 = time.process_time()
        print("Se ejecutó el requerimiento 3")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 5:
        t1 = time.process_time()
        print("Se ejecutó el requerimiento 4")
        t2 = time.process_time()
        print("El tiempo de ejecución fue de " + str(t2-t1) + " segundos")

    elif int(inputs[0]) == 8:
        ayuda={}
        for i in catalog["videos"]["elements"]:
            dato_interes=i["views"]
            ayuda[dato_interes]=i
        
        
        
            
            
                
    
    else:
        sys.exit(0)
sys.exit(0)
