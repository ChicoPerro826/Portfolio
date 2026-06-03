import math


def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b!=0:
        return a/b
    else:
        print("Syntax error(No se puede dividir por cero)")

def potenciar(a,b):
    return a ** b

def raiz_cuadrada(a):
    if a == 0:
        print("Syntax error")
    else:
        return math.sqrt(a)

def porcentaje(a,b):
    return (a * b) / 100

def operacion_a_hacer(eleccion, a, b):
    match eleccion:
        case 1:
            print(sumar(a,b))
        case 2:
            print(restar(a,b))
        case 3:
           print(multiplicar(a,b))
        case 4:
            print(dividir(a,b))
        case 5:
            print(potenciar(a,b))
        case 6:
            print(raiz_cuadrada(a))
        case 7:
            print(porcentaje(a,b))
        case 8:
            print("Saliendo del programa...")
        case _:
            print("Seleccione una opcion valida")


menu = "¿Qué operación vas a realizar?\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5 - Potencia\n6 - Raíz Cuadrada\n7 -Porcentaje\n8 - Salir del programa\n> "
eleccion = int(input(menu))
a=float(input("Cual es el primer numero a operar "))
if eleccion == 6:
    b=0.0
else:
    b=float(input("Cual es el segundo numero a operar "))

operacion_a_hacer(eleccion, a, b)