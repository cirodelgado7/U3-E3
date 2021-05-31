class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, mt, cp, ci):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mt, cp, ci)

    def opcion1(self, mt, cp, ci):
        mt.registrarInscripcion(cp, ci)

    def opcion2(self, mt, cp, ci):
        mt.consultarInscripcion()

    def opcion3(self, mt, cp, ci):
        mt.consultarPersonasInscriptas()

    def opcion4(self, mt, cp, ci):
        mt.registrarPago()

    def salir(self, mt, cp, ci):
        mt.guardarInscripciones()
        print('Las inscripciones fueron guardadas en el archivo InscripcionesGuardadas.csv')

    def mostrarMenu(self, mt, cp, ci):
        salir = False
        while not salir:
            print("\n***** Talleres de Capacitacion *****")
            print("*************** Menu ***************\n"
                  "1. Registrar inscripción"
                  "\n2. Consultar inscripción"
                  "\n3. Consultar personas inscriptas"
                  "\n4. Registrar pago"
                  "\n5. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 6) and type(op) is not str:
                self.opcion(op, mt, cp, ci)
                salir = op == 5
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')