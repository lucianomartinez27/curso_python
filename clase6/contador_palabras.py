#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("file.txt", "r")

texto = f.read()

palabras = texto.split()
length = len(palabras)

print(palabras)
print(length)
