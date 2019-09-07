
import numpy as np

def f(x):
    return (np.sin(x - 3) - x + 1)


def metodo_biseccion (putno_a, punto_b, valor_tolerancia):
    iteraciones = 0
    while np.abs(putno_a - punto_b) >= valor_tolerancia :
        punto_medio = (putno_a + punto_b) / 2
        iteraciones = iteraciones + 1
        if f(putno_a) * f(punto_medio) < 0 :
            punto_b = punto_medio
        elif f(punto_medio) * f(punto_b) < 0 :
            putno_a = punto_medio
        else :
            break
    print('resultado: ' + str(punto_medio))
    print('iteraciones: ' + str(iteraciones))

metodo_biseccion(3,7,1e-1)
