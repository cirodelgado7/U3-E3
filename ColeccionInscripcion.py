import numpy as np
from ClaseInscripcion import Inscripcion


class ManejadorI:

    __Inscripciones = None
    __cantidad = 0
    __dimension = 0
    __incremento = 0

    def __init__(self, dimension, incremento=5):
        self.__Inscripciones = np.empty(dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarInscripcion(self, unaInscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Inscripciones.resize(self.__dimension)
        self.__Inscripciones[self.__cantidad] = unaInscripcion
        self.__cantidad += 1

    def longitudArreglo(self):
        return len(self.__Inscripciones)