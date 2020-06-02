#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#sirve para pasar argumentos en la linea de comandos
from sys import argv 

#Abrimos los dos archivos
file1 = open(argv[1], 'r')
file2 = open(argv[2], 'r')

#leemos el contenido de los dos archivos abiertos
text_file1 = file1.read()
text_file2 = file2.read()
#cerramos los archivos
f.close()
f2.close()

#unimos  los textos de ambos archivos
concatenated_text = text_file1 + text_file2

#creamos un nuevo archivo
new_file = open("concatenado.txt", 'w')

#lo escribimos con el contenido guardado anteriormente
new_file.write(concatenated_text)

#cerramos el nuevo archivo
new_file.close()
