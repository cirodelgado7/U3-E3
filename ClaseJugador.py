class Jugador:
    __nombre = ''
    __dni = ''
    __ciudadNatal = ''
    __pais = ''
    __fechaNacimiento = ''

    def __init__(self, nombre='', dni='', ciudadNatal='', pais='', fechaNacimiento=''):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudadNatal = ciudadNatal
        self.__pais = pais
        self.__fechaNacimiento = fechaNacimiento

    def __str__(self):
        cadena = '\nNombre: ' + self.__nombre
        cadena += '\nD.N.I.: ' + self.__dni
        cadena += '\nCiudad Natal: ' + self.__ciudadNatal
        cadena += '\nPais: ' + self.__pais
        cadena += '\nFecha de Nacimiento: ' + self.__fechaNacimiento
        return cadena

    def getNombre(self):
        return self.__nombre

    def getDNI(self):
        return self.__dni

    def getCiudadNatal(self):
        return self.__ciudadNatal

    def getPais(self):
        return self.__pais

    def getFechaNacimiento(self):
        return self.__fechaNacimiento