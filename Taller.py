class Taller:
    __idTaller = ''
    __nombre = ''
    __vacante = 1
    __montoInscripcion = 0
    __listaInscripciones = []

    def __init__(self, idTaller='', nombre='', vacante=1, montoInscripcion=0):
        self.__idTaller = idTaller
        self.__nombre = nombre
        self.__vacante = vacante
        self.__montoInscripcion = montoInscripcion
        self.__listaInscripciones = []

    def __str__(self):
        return 'Numero de Taller: {} \nNombre del Taller: {} \nCantidad de Vacantes: {} \nMonto de Inscripcion: {}' \
            .format(self.__idTaller, self.__nombre, self.__vacante, self.__montoInscripcion)

    def getIdTaller(self):
        return self.__idTaller

    def getNombre(self):
        return self.__nombre

    def getVacante(self):
        return self.__vacante

    def setVacantes(self):
        self.__vacante -= 1

    def getMontoInscripcion(self):
        return self.__montoInscripcion

    def agregarInscripcion(self, unaInscripcion):
        self.__listaInscripciones.append(unaInscripcion)

    def consultarDNI(self, dni):
        i = 0
        r = None
        while i < len(self.__listaInscripciones) and r == None:
            if self.__listaInscripciones[i].getPersona().getDNI() == dni:
                r = self.__listaInscripciones[i]
            else:
                i += 1
        return r

    def consultarTaller(self, numero):
        i = 0
        r = None
        while i < len(self.__listaInscripciones) and r == None:
            if self.__listaInscripciones[i].getTaller().getIdTaller() == numero:
                r = self.__listaInscripciones[i]
            else:
                i += 1
        return r

    def registrarPago(self, dni):
        i = 0
        while i < len(self.__listaInscripciones) and self.__listaInscripciones[i].getPersona().getDNI() == dni:
            if self.__listaInscripciones[i].getPago():
                self.__listaInscripciones[i].setPago()
            else:
                i += 1
