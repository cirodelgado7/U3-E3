from ManejadorTalleres import ManejadorT
from ColeccionPersona import ColeccionP
from ColeccionInscripcion import ManejadorI
from MenuTalleres import Menu

if __name__ == '__main__':
    mt = ManejadorT(0)
    print(mt)
    mt.cargarTalleres()
    cp = ColeccionP()
    ci = ManejadorI(0)
    menu = Menu()
    menu.mostrarMenu(mt, cp, ci)
