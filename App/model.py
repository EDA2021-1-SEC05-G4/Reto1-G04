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
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qu
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initcatalog(tipo):
    return{"videos": lt.newList(tipo)}

def init_lista_categorias():
    return {"categorias": lt.newList('ARRAY_LIST')}

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)

def addcategory(lista, categoria):
    lt.addLast(lista["categorias"], categoria)

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
    if int(video1["views"]) > int(video2["views"]):
        x=True
    else:
        x=False
    return x

# Funciones de ordenamiento
def sortVideos(catalog, size, tipo):
    if size != "None":
        sub_list = lt.subList(catalog['videos'], 0, size)
    else:
        sub_list = catalog
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if tipo == 1:
        sorted_list = se.selection_sort(sub_list, cmpfunction)
    elif tipo == 2:
        sorted_list = it.insertion_sort(sub_list, cmpfunction)       
    elif tipo == 3:
        sorted_list = sa.shell_sort(sub_list, cmpfunction)     
    elif tipo == 4:
        sorted_list = qu.sort(sub_list, cmpfunction)
    elif tipo == 5:
        sorted_list = me.mergesort(sub_list, cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

# Funciones requerimiento 1
def categorias(lista_categoria, categoria):
    for cat in lista_categoria["categorias"]["elements"]:
        if cat["name"] == categoria:
            return cat["id"]

def saber_categoria(lista,categoria):
    j=(lista["categorias"]["elements"])
    for i in j:
        if i["id"].replace("\t","") == categoria:
            p=i["name"].replace(" ","")
            break
    return p

def video_trending_categorie(lista, categoria,lista_categoria):
    categoria_veces={}
    categoria_p1={}
    mayor=0
    respuesta =""
    for i in range(lt.size(lista["videos"])):
        objeto=lt.getElement(lista["videos"],i)
        categoria_video = objeto["category_id"]
        nombre=saber_categoria(lista_categoria,categoria_video).lower()
        if nombre == categoria.lower():
            if objeto["video_id"] in categoria_veces:
                categoria_veces[objeto["video_id"]]+=1
            else:
                categoria_veces[objeto["video_id"]]=1
                categoria_p1[objeto["video_id"]]=objeto
    for o in categoria_veces:
        if categoria_veces[o] > mayor:
            mayor=categoria_veces[o]
            respuesta=(o,categoria_veces[o])
    for h in categoria_p1:
        if respuesta[0] == h:
            entregar=categoria_p1[h]
            break

    g=(entregar["title"],entregar["channel_title"],entregar["category_id"],nombre,mayor)

    return g

            
        
        
  
def video_trending_countrie(lista, pais):
    videos={}
    videos1={}
    mayor=0
    entregar=""
    respesta=""
    for i in range(lt.size(lista["videos"])):
        objeto=lt.getElement(lista["videos"],i)
        f=objeto["country"].lower()
        if f == pais.lower():
            
            if objeto["video_id"] in videos:
                videos[objeto["video_id"]]+=1
            else:
                videos[objeto["video_id"]]=1
                videos1[objeto["video_id"]]=objeto
                
    for o in videos:
        if videos[o] > mayor:
            mayor = videos[o]
            respesta=(o,videos[o])
    for h in videos1:
        if respesta[0] == h:
            entregar=videos1[h]
            break

    g=(entregar["title"],entregar["channel_title"],entregar["country"],mayor)

    return g

        

        
