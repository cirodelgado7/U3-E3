import numpy as np
import csv
from ClaseEquipo import Equipo


class ManejadorE:
    __cantidad = 0
    __dimension = 5
    __incremento = 5

    def __init__(self, dimension=5, incremento=5):
        self.__listaEquipos = np.empty(self.__dimension, dtype=Equipo)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def __str__(self):
        s = ' '
        for lista in self.__listaEquipos:
            s += str(lista) + '\n'
        return s

    def agregarEquipo(self, unEquipo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaEquipos.resize(self.__dimension)
        self.__listaEquipos[self.__cantidad] = unEquipo
        self.__cantidad += 1

    def cargarArchivo(self):
        archivo = open('Equipos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        self.__listaEquipos.resize(int(next(reader)[0]))
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                unEquipo = Equipo(fila[0], fila[1])
                self.agregarEquipo(unEquipo)
        archivo.close()

    def obtenerListaEquipos(self):
        return self.__listaEquipos
