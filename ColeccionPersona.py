class ColeccionP:

    __listaPersonas = []

    def __init__(self):
        self.__listaPersonas = []

    def __str__(self):
        s = "\n***** Personas *****\n"
        for lista in self.__listaPersonas:
            s += str(lista) + '\n'
        return s

    def agregarPersona(self, unaPersona):
        self.__listaPersonas.append(unaPersona)
