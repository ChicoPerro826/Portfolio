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
        case _:
            print("Seleccione una opcion valida")

a=float(input("Cual es el primer numero a operar "))
b=float(input("Cual es el segundo numero a operar "))
eleccion = int(input("¿Qué operación vas a realizar?\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5- Potenciar \n> "))
operacion_a_hacer(eleccion, a, b)
