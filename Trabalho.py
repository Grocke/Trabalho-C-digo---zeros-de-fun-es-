import math
import numpy as np  
import matplotlib.pyplot as plt
from scipy.optimize	import fsolve


#Definindo uma função

def funcao(x):
    return x**2 - 6

#Definição do intervalo [a,b] e um erro 

def bisseccao(a, b, e):

    if funcao(a)*funcao(b) < 0:
        while (math.fabs(b-a)/2 > e):
            xl = (a+b)/2
            print(xl)
            print("teste: ", xl)
            if funcao(xl) == 0:
                print("Raiz é: " ,xl)                             
                break
            else:
                if funcao(a)*funcao(xl) < 0:
                    b = xl
                    print(b)
                    print("B: ", b)
                else:
                    a = xl
                    print(a)
                    print("A: ", a)
        print("Valor da raiz é: ", xl)

    else:
        print("Não há raiz neste intervalo")
bisseccao(2,3,0.01)

#Derivada
def derivada(f, x, dx = 1e-6):
    df = f(x + dx) - f(x - dx)
    return df/(2*dx)

# Metodo de Newton
def newton(f, x, tol = 0.001, maxIter = 5):

    x = x0
    fx = f(x)
    
    for _ in range(maxIter):
        
        if abs(fx) < tol:
            break

        fpx = derivada(f, x)
        if abs (fpx) < tol:
            break

        x = x - fx/fpx
        fx = f(x)
        
    return x

func = lambda x: x**2 - x - 1
x0 = 2
x = newton(func, x0, tol = 0.001, maxIter = 5)
print("Solution: x = {}, f(x) = {}".format(x, func(x)))
