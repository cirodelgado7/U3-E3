class Contrato:
    __fechaInicio = ''
    __fechaFin = ''
    __pagoMensual = ''
    __equipo = None
    __jugador = None

    def __init__(self, fechaInicio='', fechaFin='', pagoMensual='', equipo=None, jugador=None):
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__pagoMensual = pagoMensual
        self.__equipo = equipo
        self.__jugador = jugador

    def __str__(self):
        cadena = '\nFecha de Inicio: ' + "{0}/{1}/{2}".format(self.__fechaInicio.day,self.__fechaInicio.month, self.__fechaInicio.year)
        cadena += '\nFecha de Fin: ' + str(self.__fechaFin)
        cadena += '\nPago Mensual: ' + self.__pagoMensual
        cadena += str(self.__equipo)
        cadena += str(self.__jugador)
        return cadena

    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFin(self):
        return self.__fechaFin

    def getPagoMensual(self):
        return self.__pagoMensual

    def getEquipo(self):
        return self.__equipo

    def getJugador(self):
        return self.__jugador


