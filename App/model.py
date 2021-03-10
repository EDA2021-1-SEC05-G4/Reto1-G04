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
    a = {"videos": lt.newList(tipo),
           "categorias": lt.newList(tipo),
           "tags": lt.newList(tipo)}
    return a

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)

def addcategory(catalog, categoria):
    lt.addLast(catalog["categorias"], categoria)

def addtag(catalog, video):
    lt.addLast(catalog["tags"], video)

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
        return 1
     elif int(video1["likes"]) < int(video2["likes"]):
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
def categorias(catalog, categoria):
    categorias = catalog["categorias"]
    for i in range(lt.size(categorias)):
        a = lt.getElement(categorias,i)
        if categoria.lower() in a["name"].lower():
            return a["id"]

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

    g={"title": entregar["title"],"channel_title":entregar["channel_title"],
        "category_id":entregar["category_id"],"dias_tendencia":mayor}

    return g

def video_tendencia_pais(catalog, pais):
    videos = catalog["videos"]
    sortVideos(videos, "None", 4, cmpfunction)

    videos_pais = {}
    tendencia_videos = {}
    for i in range(lt.size(videos)):   
        video = lt.getElement(videos, i)
        if video["country"].lower() == pais.lower():
            if video["video_id"] in tendencia_videos:
                tendencia_videos[video["video_id"]] = tendencia_videos[video["video_id"]] + 1
            else:
                info = {"title":video["title"],"channel_title":video["channel_title"], "country": pais}
                tendencia_videos[video["video_id"]] = 1
                videos_pais[video["video_id"]]= info

    idvideo_tendencia = ""
    mas_dias = 0
    for i in tendencia_videos:
        if tendencia_videos[i] > mas_dias:
            mas_dias = tendencia_videos[i]
            idvideo_tendencia = i

    video_tp = videos_pais[idvideo_tendencia]
    video_tp["dias_tendencia"] = mas_dias

    return video_tp

def videos_categoria_pais(catalog, categoria, pais, numero):
    videos = catalog["videos"]
    categoria = categorias(catalog,categoria)
    sortVideos(videos, "None", 4, cmpfunction)
    lista_videos = lt.newList(datastructure='ARRAY_LIST')

    for i in range(lt.size(videos)):
        video = lt.getElement(videos, i)
        if video["category_id"] == categoria:
            if video["country"] == pais:
                while numero > 0:
                    vid_t = {"Nombre del video": video["title"], "Trending date": video["trending_date"],
                        "Nombre del canal": video["channel_title"], "Fecha Publicación": video["publish_time"],
                        "Reproducciones": video["views"], "Likes": video["likes"], "Dislikes": video["dislikes"]}
                    lt.addLast(lista_videos, vid_t)
                    numero-=1

    return lista_videos

def videos_likes(pais, tag, numero):
    videos = catalog["videos"]
    tags = catalog["tags"]
    sortVideos(videos, "None", 4, comparelikes)    
    quitar_llaves = ["comment_count","thumbnail_link","comments_disabled","ratings_disabled",\
                    "video_error_or_removed","description", "category_id", "trending_date"]

    lista_videos = lt.newList(datastructure='ARRAY_LIST')
    for i in range(lt.size(videos)):
        video = lt.getElement(videos, i)
        for llave in quitar_llaves:
            del video[llave] 
        if video["country"] == pais:
            video_tag = tags["video_id"]
            for e in range(lt.size(video_tag)):
                if tag in e:
                    del video["country"]
                    del video["video_id"]
                    del video["category_id"]
                    lt.addLast(video)

    lista_videos = lt.sub_list(lista_videos, 0, numero)
    return lista_videos

        

        
