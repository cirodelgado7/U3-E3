import csv
from ClaseJugador import Jugador


class ManejadorJ:
    __listaJugadores = []

    def __init__(self):
        self.__listaJugadores = []

    def __str__(self):
        s = ' '
        for lista in self.__listaJugadores:
            s += str(lista) + '\n'
        return s

    def cargarArchivo(self):
        archivo = open('Jugadores.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                unJugador = Jugador(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listaJugadores.append(unJugador)
        archivo.close()

    def obtenerListaJugadores(self):
        return self.__listaJugadores

