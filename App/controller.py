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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros y de categorias
def initcatalog(tipo):
    catalog = model.initcatalog(tipo)
    return catalog

def init_lista_categorias():
    lista = model.init_lista_categorias()
    return lista

# Funciones para la carga de datos
def cargardatos(catalog):
    vfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addvideo(catalog, video)

def cargar_categorias(lista):
    cfile = cf.data_dir + 'videos/category-id.csv'
    archivo = open(cfile, "r", encoding="utf-8")
    lista_titulos = ["id", "name"]
    print(lista_titulos)
    
    linea = archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        categoria = {}
        datos = linea.strip().split(" ")
        categoria[lista_titulos[0]] = datos[0]
        nombre = ""
        e = 1
        while e < len(datos):
            nombre = nombre + " " + datos[e]
            e+=1
        categoria[lista_titulos[1]] = nombre
        linea = archivo.readline()
        model.addcategory(lista, categoria)
    archivo.close()

# Funciones de ordenamiento
def sortVideos(catalog, size, tipo):
    return model.sortVideos(catalog, size, tipo)

# Funciones de consulta sobre el catálogo
def funcion_lista(lista):
    x=model.tipo_de_lista(lista)
    return x

# Funcion requerimiento 1
def videos_categoria_pais(lista, catalog, categoria, pais, numero):
    return model.videos_categoria_pais(lista, catalog, categoria, pais, numero)

def video_tendencia_pais(catalog, pais):
    return model.video_tendencia_pais(catalog, pais)
