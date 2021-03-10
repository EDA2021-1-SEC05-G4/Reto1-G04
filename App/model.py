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
    a = {"videos": lt.newList(tipo, cmpfunction = cmpfunction),
           "categorias": lt.newList(tipo)}
    return a

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)

def addcategory(catalog, categoria):
    lt.addLast(catalog["categorias"], categoria)

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

def categorias(catalog, categoria):
    categorias = catalog["categorias"]
    for i in range(lt.size(categorias)):
        a = lt.getElement(categorias,i)
        if categoria.lower() in a["name"].lower():
            return a["id"]

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpfunction(video1, video2):
    if int(video1["views"]) > int(video2["views"]):
        x=True
    elif int(video1["views"])<int(video1["views"]):
        x=False
    else:
        x=True
    return x

def cmpviews(video1, video2):
    if int(video1["views"]) > int(video2["views"]):
        x=1
    elif int(video1["views"])<int(video1["views"]):
        x=-1
    else:
        x=0
    return x

def comparevideosid(video1,video2):
    if video1["video_id"] > video2["video_id"]:
        return 1
    elif video1["video_id"] < video2["video_id"]:
        return -1
    else:
        return 0   

def comparelikes(video1, video2):
     if int(video1["likes"]) > int(video2["likes"]):
        return True
     else:
        return False 

def comparetendency(video1, video2):
     if int(video1["Dias Tendencia"]) > int(video2["Dias Tendencia"]):
        return 1
     elif int(video1["Dias Tendencia"]) < int(video2["Dias Tendencia"]):
        return -1
     else:
        return 0    

def comparetitle(video1, video2):
     if video1["title"] > video2["title"]:
        return 1
     elif video1["title"] < video2["title"]:
        return -1
     else:
        return 0  


# Funciones de ordenamiento
def sortVideos(catalog, size, tipo, cmpfunction):
    if size != "None":
        sub_list = lt.subList(catalog['videos'], 0, size)
    else:
        sub_list = catalog
    sub_list = sub_list.copy()
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
    return  sorted_list

# Funciones requerimientos

#funcion requerimiento 1
def videos_categoria_pais(catalog, categoria, pais, numero):
    videos = sortVideos(catalog["videos"], "None", 4, cmpviews)
    categoria = categorias(catalog,categoria)
    lista_videos = lt.newList(datastructure='ARRAY_LIST')

    for i in range(1, lt.size(videos)):
        video = lt.getElement(videos, i)
        if video["category_id"] == categoria:
            if video["country"].lower() == pais.lower():
                if numero > 0:
                    vid_t = {"Nombre del video": video["title"], "Trending date": video["trending_date"],
                        "Nombre del canal": video["channel_title"], "Fecha Publicación": video["publish_time"],
                        "Reproducciones": video["views"], "Likes": video["likes"], "Dislikes": video["dislikes"]}
                    lt.addLast(lista_videos, vid_t)
                    numero-=1
                elif numero == 0:
                    break
                    
    return lista_videos

#funcion requerimiento 2
def video_tendencia_pais(catalog, pais):
    videos_pais = {}
    tendencia_videos = {}
    for i in range(1, lt.size(catalog["videos"])):   
        video = lt.getElement(catalog["videos"], i)
        if video["country"].lower() == pais.lower():
            if video["video_id"] in tendencia_videos:
                tendencia_videos[video["video_id"]] = tendencia_videos[video["video_id"]] + 1
            else:
                tendencia_videos[video["video_id"]] = 1
                videos_pais[video["video_id"]]= video

    mas_dias = 0
    video = {}
    for i in tendencia_videos:
        if tendencia_videos[i] > mas_dias:
            mas_dias = tendencia_videos[i]
            video = videos_pais[i]

    video["Dias Tendencia"] = mas_dias
    return video

#funcion requerimiento 3
def video_tendencia_categoria(catalog, categoria):
    idcategoria = categorias(catalog, categoria)
    categoria_veces={}
    categoria_p1={}
    mayor=0
    respuesta =""
    entregar = ""

    for i in range(lt.size(catalog["videos"])):
        objeto=lt.getElement(catalog["videos"],i)
        if objeto["category_id"] == idcategoria:
            if objeto["video_id"] in categoria_veces:
                categoria_veces[objeto["video_id"]]=categoria_veces[objeto["video_id"]]+1
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

    return  (entregar["title"], entregar["channel_title"],entregar["category_id"], mayor)

#funcion requerimiento 4
def videos_likes(catalog, pais, tag, numero):
    videos_pais = lt.newList(datastructure="ARRAY_LIST")

    for i in range(1, lt.size(catalog["videos"])):
        video = lt.getElement(catalog["videos"], i)
        if video["country"].lower() == pais.lower():
            lista_tag = video["tags"]
            for e in range(len(lista_tag)):
                if tag in lista_tag[e]:
                    lt.addLast(videos_pais,video)

    videos = sortVideos(videos_pais, "None", 4, comparelikes)
    vids = lt.subList(videos, 1, numero)
    respuesta = lt.newList()

    for i in range(1, lt.size(vids)):
        video = lt.getElement(vids, i)
        vid_t = {"Nombre del video": video["title"], "Nombre del canal": video["channel_title"],
                "Fecha Publicación": video["publish_time"],"Reproducciones": video["views"], 
                        "Likes": video["likes"], "Dislikes": video["dislikes"], "Tags": video["tags"]}
        lt.addLast(respuesta, vid_t)

    return respuesta

        

        
