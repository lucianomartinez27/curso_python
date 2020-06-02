#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from persona import Persona

persona1 = Persona(38262759)

persona1.nombre = 'Luciano'
persona1.apellido = 'Martinez'
persona1.profesion = 'Apicultor'
persona1.edad = 25

print(persona1)

persona1.mayor_de_edad()

persona1.ver_dni()
