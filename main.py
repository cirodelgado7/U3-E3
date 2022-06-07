from datetime import date
from ManejadorEquipos import ManejadorE
from ManejadorJugadores import ManejadorJ
from ManejadorContratos import ManejadorC
from ClaseContrato import Contrato


def test(me, mj, mc):
    listaJugadores = mj.obtenerListaJugadores()
    listaEquipos = me.obtenerListaEquipos()
    c1 = Contrato(date(2022, 5, 26), date(2022, 11, 26), '2000000', listaEquipos[0], listaJugadores[0])
    c2 = Contrato(date(2022, 5, 26), date(2022, 11, 26), '2000000', listaEquipos[0], listaJugadores[1])
    c3 = Contrato(date(2022, 5, 26), date(2022, 11, 26), '2000000', listaEquipos[1], listaJugadores[2])
    c4 = Contrato(date(2022, 5, 26), date(2022, 11, 26), '2000000', listaEquipos[1], listaJugadores[3])
    mc.agregarContrato(c1)
    mc.agregarContrato(c2)
    mc.agregarContrato(c3)
    mc.agregarContrato(c4)
    print(mc)
    mc.consultarContratos(input('D.N.I.: '))
    mc.consultarFechas(input('Nombre del Equipo: '))
    mc.calcularImporte(input('Nombre del Equipo: '))
    mc.guardarArchivo()


if __name__ == '__main__':
    me = ManejadorE()
    me.cargarArchivo()
    print(me)
    mj = ManejadorJ()
    mj.cargarArchivo()
    mc = ManejadorC(4)
    test(me, mj, mc)
