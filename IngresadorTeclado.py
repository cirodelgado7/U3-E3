import re
from datetime import date


class IngresadorTeclado:
    __valor = None

    def __init__(self):
        self.__valor = None

    def inputInt(self, mensaje: str, mensajeError="El dato debe ser un entero, reingrese el valor: ") -> int:
        self.__valor = input(mensaje)
        band = True
        while band:
            try:
                self.__valor = int(self.__valor)
            except:
                self.__valor = input(mensajeError)
            else:
                band = False

        return self.__valor

    def inputFloat(self, mensaje: str,
                   mensajeError="El dato debe ser un decimal con punto, reingrese el valor: ") -> float:
        self.__valor = input(mensaje)
        band = True
        while band:
            try:
                self.__valor = float(self.__valor)
            except:
                self.__valor = input(mensajeError)
            else:
                band = False

        return self.__valor

    def inputRegularExpression(self, mensaje: str, expresionRegular: str,
                               mensajeError="Dato invalido, reintente: ") -> str:
        self.__valor = input(mensaje)
        while re.fullmatch(expresionRegular, self.__valor) is None:
            self.__valor = input(mensajeError)
        return self.__valor

    def inputFecha(self, mensaje: str, mensajeError="Fecha invalida, reintente: ") -> date:
        """Solicita el ingreso de una fecha en el formato dd/mm/aaaa hasta ingresar una 
        valida y retorna un objeto del tipo date"""
        fecha = None
        valor = self.inputRegularExpression(mensaje, "[0-9]{2,2}/[0-9]{2,2}/[0-9]{4,4}", mensajeError)
        while fecha == None:
            valores = (int(valor[0:2]), int(valor[3:5]), int(valor[6:10]))
            try:
                fecha = date(valores[2], valores[1], valores[0])
            except:
                valor = self.inputRegularExpression(mensajeError, "[0-9]{2,2}/[0-9]{2,2}/[0-9]{4,4}", mensajeError)
        return fecha
