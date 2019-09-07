import numpy as np

def f(x):
    return (np.sin(x - 3) - x + 1)

def f_prima(x):
    return np.cos(x - 3) - 1

def metodo_newton(punto_inicial, valor_tolerancia):

    punto_a_evaluar = punto_inicial - (f(punto_inicial)/f_prima(punto_inicial))  
    iteraciones = 0
    while (np.abs(punto_a_evaluar - punto_inicial) >= valor_tolerancia):
        punto_inicial = punto_a_evaluar
        iteraciones = iteraciones + 1
        #cuidado puede caer en division por 0
        punto_a_evaluar = punto_inicial - (f(punto_inicial)/f_prima(punto_inicial))
    
    print('iteraciones: ' + str(iteraciones))
    print('respuesta: ' + str(punto_a_evaluar))

metodo_newton(1,1e-7)