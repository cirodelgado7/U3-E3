class Inscripcion:

    __fechaInscripcion = ''
    __pago = False
    __persona = ''
    __taller = ''

    def __init__(self, fechaInscripcion, pago, persona, taller):
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def __str__(self):
        return '\nFecha de Inscripción: {} \nPago: {} \n{} \n{}'\
            .format(self.__fechaInscripcion, self.__pago, self.__persona, self.__taller)

    def getPersona(self):
        return self.__persona

    def getTaller(self):
        return self.__taller

    def getFechaInscripcion(self):
        return self.__fechaInscripcion

    def getPago(self):
        return self.__pago

    def setPago(self):
        self.__pago = True
