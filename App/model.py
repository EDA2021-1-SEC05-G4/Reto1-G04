"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import sys
sys.path.append("DISClib")
from ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as it
from DISClib.Algorithms.Sorting import selectsort as se
from DISClib.Algorithms.Sorting import quicksort as qu
from DISClib.Algorithms.Sorting import mergesort as me
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initcatalog(tipo):
    return{"videos": lt.newList(tipo)}

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)

# Funciones para creacion de datos

def muestra(lista,pos,nume):
    u=lt.subList(lista,pos,nume)
    return u


# Funciones de consulta

def tipo_de_lista(lista):
    if lista == 1:
        k='ARRAY_LIST'
    elif lista == 2:
        k='LINKED_LIST'
    else:
        k = "Ninguno"
    return k

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpfunction(video1, video2):
    x=False
    if video1["views"] > video2["views"]:
        x=True
    return x

# Funciones de ordenamiento
def sortVideos(catalog, size, tipo):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if tipo == 1:
        sorted_list = se.selection_sort(sub_list, cmpfunction)
    elif tipo == 2:
        sorted_list = it.insertion_sort(sub_list, cmpfunction)       
    elif tipo == 3:
        sorted_list = sa.shell_sort(sub_list, cmpfunction)     
    elif tipo == 4:
        sorted_list = qu.quicksort(sub_list, cmpfunction)
    elif tipo == 5:
        sorted_list = me.mergesort(sub_list, cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list