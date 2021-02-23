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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initcatalog(tipo):
    k='ARRAY_LIST'
    if tipo == 1:
        k='ARRAY_LIST'
    elif tipo == 2:
        k='ARRAY_LIST'
    return{"videos": lt.newList(k)}

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)

# Funciones para creacion de datos

def muestra(lista,pos,nume):
    u=lt.subList(lista,pos,nume)
    return u

    
    

# Funciones de consulta

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

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpfunction(video1, video2):
    x=False
    if video1 < video2:
        x=True
    return x


# Funciones de ordenamiento
def selection_sort(lst):
    
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst["videos"], pos2),
               (lt.getElement(lst["videos"], minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

def insertion_sort(lst, lessfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (lessfunction(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst
def shell_sort(lst, lessfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and lessfunction(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst
