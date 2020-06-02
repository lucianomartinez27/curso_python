#!/usr/bin/env/ python3
#-*- coding: utf-8 -*-

class Alumno:
    def __init__(self, nlegajo, *notas):
        self.nlegajo = nlegajo
        self.notas_parciales = *notas
        self.nota_promedio = nota_promedio()
    def nota_promedio(self):
        total = 0
        for i in self.notas_parciales:
            total += i
        return total/len(self.notas_parciales)
    def estado_alumno(self):
        if self.nota_promedio < 6:
            print('Alumno libre')
        elif self.nota_promedio <= 8:
            print('Alumno regular')
        else:
            print('Alumno promocionado')
