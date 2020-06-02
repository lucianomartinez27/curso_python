#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 Desarrolle un nuevo módulo que tenga como salida la tabla de multiplicar del
8.:
"""

print("="*25)
print("Tabla de multiplicar del 8")
print("="*25)

lista_num_en_letras = "cero uno dos tres cuatro cinco seis siete ocho nueve".split()

for i in range(1,10):
    mul = i*8
    print(lista_num_en_letras[i], "x ocho:", "octal:", oct(mul), "hexadecimal:", hex(mul),"binario:", bin(mul))

print("="*25)
