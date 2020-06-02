#! /usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("file.txt", "r")
texto = f.read()
f.close()

nf = open("newfile.txt", "w")
nf.write(texto.upper())
nf.close()

nf = open("newfile.txt", "r")
texto2 = nf.read()
nf.close()
print(texto2)

