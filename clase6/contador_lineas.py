#! /usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("file.txt", "r")

contador = 0
for linea in f :
    contador+=1
print(contador)

