


import config as cf
import sys
sys.path.append("DISClib")
from ADT import list as lt
from Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initcatalog(tipo_losto):
    if tipo_losto == 1:
        k="ARRAY_LIST"
    elif tipo_losto == 2:
        k="LINKED_LIST"
    return{"videos": lt.newList(k)}

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def less(element1, element2, column=columna): # Agregué "column" para poder escoger, por ejemplo, entre vote_average y vote_count
    if float(element1[column]) < float(element2[column]):
        return True
    return False
def greater(element1, element2,column=columna):
    if float(element1[column]) > float(element2[column]):
        return True
    return False



# Funciones de ordenamiento

def selectionSort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst, pos2),
               (lt.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

def insertionSort(lst, lessfunction):
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

def shellSort(lst, lessfunction):
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

def ordenar(function, lst, criteria):

        
    t1_start = process_time() #tiempo inicial
    if function == "selectionsort":
        if criteria == a:
            selectionSort(lst,greater)
       elif criteria == b:
           selectionSort(lst,less)
    if function == "insertionsort":
        if criteria == a :
            insertionSort(lst,greater)
        elif criteria == b:
            insertionSort(lst,less)
    if function == "shellsort":
        if criteria == a:
            shellSort(lst,greater)
        elif criteria == b:
            shellSort == (lst,less)
    i = 0
    ordenado = []
    while i < len(lst):
       i += 1
       pelicula = lt.getElement(lst,i)
       ordenado.append(pelicula)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")       
    return ordenado

def cmpVideosByViews(video1, video2):

    if float(video1["views"]) < float(video2["videos"]):
        respuesta= True
    else:
        respuesta = False
    return respuesta

def crear_sublista (lista,posicion_inicial,muestra):
    nueva_lista=[]
    tamaño_restante = float(posicion_inicial-len(lista))
    if tamaño_restante >= float(muestra) :
        nueva_lista=lista[posicion_inicial:(posicion_inicial+muestra)]
    else:
        while float(muestra) > float(tamaño_restante):
            muestra=float(input("porfavor cambia la muestra , excede a los datos cargados") )
            if float(tamaño_restante) >= float(muestra):
                nueva_lista=lista[posicion_inicial:(posicion_inicial+muestra)]
    return nueva_lista
