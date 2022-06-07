import numpy as np
import csv
from datetime import date, timedelta
from ClaseContrato import Contrato


class ManejadorC:
    __listaContratos = None
    __cantidad = 0
    __dimension = 0
    __incremento = 0

    def __init__(self, dimension, incremento=5):
        self.__listaContratos = np.empty(dimension, dtype=Contrato)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def __str__(self):
        s = ''
        for lista in self.__listaContratos:
            s += str(lista) + '\n'
        return s

    def agregarContrato(self, unContrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaContratos.resize(self.__dimension)
        self.__listaContratos[self.__cantidad] = unContrato
        self.__cantidad += 1

    def consultarContratos(self, dni):
        for contrato in self.__listaContratos:
            if contrato.getJugador().getDNI() == dni:
                print('Nombre del Equipo: {}'.format(contrato.getEquipo().getNombre()))
                print('Fecha de Finalización del Contrato: {}'.format(contrato.getFechaFin()))

    def consultarFechas(self, nombreEquipo):
        for contrato in self.__listaContratos:
            if contrato.getEquipo().getNombre() == nombreEquipo:
                if (contrato.getFechaFin() - date.today())//timedelta(days=30):
                    print('\nNombre: {}\nD.N.I.: {}\nCiudad Natal: {}\nPais: {}\nFecha de Nacimiento: {}'
                          .format(contrato.getJugador().getNombre(), contrato.getJugador().getDNI(),
                                  contrato.getJugador().getCiudadNatal(), contrato.getJugador().getPais(),
                                  contrato.getJugador().getFechaNacimiento()))

    def calcularImporte(self, nombreEquipo):
        importe = 0
        for contrato in self.__listaContratos:
            if contrato.getEquipo().getNombre() == nombreEquipo:
                importe += int(contrato.getPagoMensual())
        print('El importe total de los contratos es: ${}'.format(importe))

    def guardarArchivo(self):
        archivo = open('Contratos.csv', 'w', newline='')
        writer = csv.writer(archivo, delimiter=';')
        for contrato in self.__listaContratos:
            writer.writerow({contrato.getJugador().getDNI(): 1,
                             contrato.getEquipo().getNombre(): 2,
                             contrato.getFechaInicio(): 3,
                             contrato.getFechaFin(): 4,
                             contrato.getPagoMensual(): 5})


