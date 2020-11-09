#Ejercicio 4 tarea, Martin José Pérez Gálvez

import random
from tabulate import tabulate



#Funciones
#Funciones principal
def funcion(x,y):
    return ((x + 2*y - 7)*(x + 2*y - 7))+((2*x + y - 5)*(2*x + y - 5))

#Derivadas parciales
def dxfuncion(x,y):
    return 10*x + 8*y - 34

def dyfuncion(x,y):
    return 8*x + 10*y - 38

#Gradientes
def desGradientex(a,x,y):
    return x - (a*dxfuncion(x,y))

def desGradientey(a,x,y):
    return y - (a*dyfuncion(x,y))

#Calcular valor minimo
def minimum_value(x,y):

    #Primera ronda de iteraciones α = 0.2
    tabla = [['α', 'x', 'y', 'dx', 'dy', 'xfinal', 'yfinal', 'f(xfinal,yfinal)']]
    a = 0.2
    for i in range(5):
        xfinal = desGradientex(a, x, y)
        yfinal = desGradientey(a, x, y)
        tabla.append([a, x, y, dxfuncion(x, y), dyfuncion(x, y), xfinal, yfinal, funcion(xfinal, yfinal)])
        x = xfinal
        y = yfinal

    #Segunda ronda de iteraciones α = 0.1
    a = 0.1
    for i in range(5):
        xfinal = desGradientex(a, x, y)
        yfinal = desGradientey(a, x, y)
        tabla.append([a, x, y, dxfuncion(x, y), dyfuncion(x, y), xfinal, yfinal, funcion(xfinal,yfinal)])
        x = xfinal
        y = yfinal

    #Tercer ronda de iteraciones α = 0.05
    a = 0.05
    for i in range(5):
        xfinal = desGradientex(a, x, y)
        yfinal = desGradientey(a, x, y)
        tabla.append([a, x, y, dxfuncion(x, y), dyfuncion(x, y), xfinal, yfinal, funcion(xfinal,yfinal)])
        x = xfinal
        y = yfinal

    #Cuarta ronda de iteraciones α = 0.01
    a = 0.01
    for i in range(10):
        xfinal = desGradientex(a, x, y)
        yfinal = desGradientey(a, x, y)
        tabla.append([a, x, y, dxfuncion(x, y), dyfuncion(x, y), xfinal, yfinal, funcion(xfinal,yfinal)])
        x = xfinal
        y = yfinal

    return tabla


def main():
    i=1
    while i <= 5:
        print('--------------------------------------------------------------  Tabla', i, '  --------------------------------------------------------------')
        print(tabulate(minimum_value(random.randint(-10, 10), random.randint(-10, 10))))
        i = i+1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


