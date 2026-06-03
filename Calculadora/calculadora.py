def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a/b

def operacion_a_hacer(eleccion, a, b):
    match eleccion:
        case "multiplicacion":
            multiplicar(a,b)
        case "suma":
            sumar(a,b)
        case "resta":
            restar(a,b)
        case "division":
            dividir(a,b)


a=float(input("Cual es el primer numero a operar"))
b=float(input("Cual es el segundo numero a operar"))
eleccion = str(input("Que operacion vas a realizar?" ))