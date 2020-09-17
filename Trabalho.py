import math
import numpy as np  
import matplotlib.pyplot as plt
from scipy.optimize	import fsolve

#Definindo uma função

def funcao(x):
    return x**2 - 6

#Metodo Bissecção
#Definição do intervalo [a,b] e um erro 

def bisseccao(a, b, e):
    if funcao(a)*funcao(b) < 0:
        while (math.fabs(b-a)/2 > e):
            xl = (a+b)/2
            print(xl)
            if funcao(xl) == 0:
                print("Raiz é: " ,xl)
                break
            else:
                if funcao(a)*funcao(xl) < 0:
                    b = xl
                    print(b)
                else:
                    a = xl
                    print(a)
        print("Valor da raiz é: ", xl)

    else:
        print("Não há raiz neste intervalo")

bisseccao(2,3,0.01)
