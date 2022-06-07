class Equipo:
    __nombre = ''
    __ciudad = ''

    def __init__(self, nombre='', ciudad=''):
        self.__nombre = nombre
        self.__ciudad = ciudad

    def __str__(self):
        cadena = '\nNombre: ' + self.__nombre
        cadena += '\nCiudad: ' + self.__ciudad
        return cadena

    def getNombre(self):
        return self.__nombre

    def getCiudad(self):
        return self.__ciudad
