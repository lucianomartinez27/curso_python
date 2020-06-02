#! /usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("file.txt", "r")

texto = f.read()

contador= 0
for i in texto:
     if i in "aeiouAEIOU":
        contador+= 1
print(contador)
