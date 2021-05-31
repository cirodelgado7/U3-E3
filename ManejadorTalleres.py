import csv
import numpy as np
from Taller import Taller
from ClaseInscripcion import Inscripcion
from ClasePersona import Persona


class ManejadorT:
    __talleres = None
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__talleres = None
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def cargarTalleres(self):
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        i = 0
        for fila in reader:
            if bandera:
                self.__talleres = np.empty(int(fila[0]), dtype=Taller)
                bandera = not bandera
            else:
                idTaller = int(fila[0])
                nombre = fila[1]
                vacantes = int(fila[2])
                montoInscripcion = int(fila[3])
                unTaller = Taller(idTaller, nombre, vacantes, montoInscripcion)
                self.__talleres[i] = unTaller
                i += 1
        archivo.close()


    def buscarTaller(self, indice):
        return self.__talleres[indice - 1]

    def registrarInscripcion(self, cp, ci):
        print("\n***** 1. Registrar inscripcion *****")
        t = self.buscarTaller(int(input("Numero de taller: ")))
        if t.getVacante() >= 1:
            t.setVacantes()
            p = Persona(input("Nombre: "), input("Direccion: "), input("DNI: "))
            cp.agregarPersona(p)
            i = Inscripcion('19/05/21', False, p, t)
            t.agregarInscripcion(i)
            ci.agregarInscripcion(i)
        else:
            print('No hay vacante para este curso')

    def consultarInscripcion(self):
        print('\n***** 2. Consultar inscripción *****')
        dni = input('Ingrese el DNI: ')
        for taller in self.__talleres:
            inscripcion = taller.consultarDNI(dni)
            if inscripcion != None:
                if inscripcion.getPago() is True:
                    print('Nombre del Taller: {} \nMonto adeudado: ${}'
                          .format(taller.getNombre(), taller.getMontoInscripcion() - taller.getMontoInscripcion()))
                else:
                    print('Nombre del Taller: {} \nMonto adeudado: ${}'
                          .format(taller.getNombre(), taller.getMontoInscripcion()))

    def consultarPersonasInscriptas(self):
        print('\n***** 3. Consultar personas inscriptas *****')
        numero = int(input('Ingrese el Numero de Taller: '))
        for taller in self.__talleres:
            inscripcion = taller.consultarTaller(numero)
            if inscripcion is not None:
                print('Nombre: {} \nDirección: {} \nDNI: {}'
                      .format(inscripcion.getPersona().getNombre(), inscripcion.getPersona().getDireccion(), inscripcion.getPersona().getDNI()))

    def registrarPago(self):
        print('\n***** 2. Registrar pago *****')
        dni = input('Ingrese el DNI: ')
        for taller in self.__talleres:
            inscripcion = taller.consultarDNI(dni)
            if inscripcion != None:
                inscripcion.setPago()
                if inscripcion.getPago():
                    print('El pago se realizó con éxito')
                else:
                    print('No fue posible realizar el pago')

    def guardarInscripciones(self):
        with open('InscripcionesGuardadas.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for taller in self.__talleres:
                inscripcion = taller.consultarTaller(int(taller.getIdTaller()))
                if inscripcion is not None:
                    writer.writerow([inscripcion.getPersona().getDNI(),
                                     inscripcion.getTaller().getIdTaller(),
                                     inscripcion.getFechaInscripcion(),
                                     inscripcion.getPago()])
            f.close()
