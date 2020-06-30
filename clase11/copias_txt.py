#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Codificar un módulo que permita posicionarse en distintos directorios del SO
mediante el módulo os. En cada directorio, liste los archivos con extensión TXT y realice
una copia en un directorio temporal (BACK). Guardar el archivo del módulo con el nombre
copias_txt.py

Al módulo, agregele la posibilidad de pasarle parametros para cambiar
el comportamiento en ejecución. Por ejemplo, extensión de archivos, directorio de backup,
etc
"""

from glob import glob
import os
import sys

os.chdir('/')
while True:
    try:
        directorio = input("Escribe la ruta del directiorio: \n") 
        os.chdir(directorio)
        break
    except FileNotFoundError:
        print("'{}', no es una ruta válida".format(directorio))

if sys.argv:
    try:
        carpeta_back = sys.argv[1]
        os.mkdir(carpeta_back)
    except FileExistsError:
        pass
    lista_archivos = glob('*{}'.format(sys.argv[2]))
    print(lista_archivos)
else:
    try:
        carpeta_back = 'BACK'
        os.mkdir(carpeta_back)
    except FileExistsError:
        pass
    lista_archivos = glob('*.txt')

for archivo in lista_archivos:
    with open(archivo, 'r') as f:
        contenido_archivo = f.read()
    with open('./{}/{}'.format(carpeta_back, archivo), 'w') as nf:
        nf.write(contenido_archivo)
        nf.close
