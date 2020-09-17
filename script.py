from tkinter import *

from math import floor, log10
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

            if funcao(xl) == 0:                                         
                break
            else:
                if funcao(a)*funcao(xl) < 0:
                    b = xl
                    
                else:
                    a = xl
                    
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



root = Tk()
root.title("Calculadora C.N")

hidden_newton = True
hidden_biseccao = False

def botao_newton():
    global hidden_newton
    hidden_newton = False
    metodo3.grid_remove()
    metodo2.grid()
    eps.grid_remove()
    B.grid()
    inter.grid_remove()
    x0.grid()
    inter1.grid_remove()
    interacao.grid()
    hidden_biseccao = True


def botao_biseccao():
    global hidden_biseccao
    hidden_biseccao = False
    metodo2.grid_remove()
    metodo3.grid()
    B.grid_remove()
    eps.grid()
    x0.grid_remove()
    inter.grid()
    interacao.grid_remove()
    inter1.grid()

    hidden_newton = True
    

valor1 = Button(root,text="Método de Newton",width=35,borderwidth=5, command=botao_newton)
valor1.grid(row=1,column=0)

valor2 = Button(root,text="Método de Bisecção",width=35,borderwidth=5, command=botao_biseccao)
valor2.grid(row=1,column=1)

metodol = Label(root, text = 'Método:', font=('calibre',10, 'bold')) 
metodol.grid(row=2,column=0,padx=10,pady=10,sticky=E)


metodo2 = Label(root, text = 'Newton', font=('calibre',10, 'bold')) 
metodo2.grid(row=2,column=1,padx=10,pady=10,sticky=W)

metodo3 = Label(root, text = 'Biseccao', font=('calibre',10, 'bold')) 
metodo3.grid(row=2,column=1,padx=10,pady=10,sticky=W)
metodo2.grid_remove()

fx1 = Label(root, text = 'f(x)', font=('calibre',10, 'bold')) 
fx1.grid(row=3,column=0,padx=10,pady=10,sticky=E)

fxentry = Entry(root,width=35,borderwidth=5)
fxentry.grid(row=3,column=1)

eps = Label(root, text = 'Epsolon', font=('calibre',10, 'bold')) 
eps.grid(row=4,column=0,padx=10,pady=10,sticky=E)

B = Label(root, text = 'B', font=('calibre',10, 'bold')) 
B.grid(row=4,column=0,padx=10,pady=10,sticky=E)
B.grid_remove()

epsentry = Entry(root,width=35,borderwidth=5)
epsentry.grid(row=4,column=1)

inter = Label(root, text = 'De:', font=('calibre',10, 'bold')) 
inter.grid(row=5,column=0,padx=10,pady=10,sticky=E)

x0 = Label(root, text = 'x0', font=('calibre',10, 'bold')) 
x0.grid(row=5,column=0,padx=10,pady=10,sticky=E)
x0.grid_remove()

interentry = Entry(root,width=35,borderwidth=5)
interentry.grid(row=5,column=1)

inter1 = Label(root, text = 'Até:', font=('calibre',10, 'bold')) 
inter1.grid(row=6,column=0,padx=10,pady=10,sticky=E)

interacao = Label(root, text = 'Interação:', font=('calibre',10, 'bold')) 
interacao.grid(row=6,column=0,padx=10,pady=10,sticky=E)
interacao.grid_remove()

interentry1 = Entry(root,width=35,borderwidth=5)
interentry1.grid(row=6,column=1)

calculate = Button(root,text="Calcular", padx=100,pady=5)
calculate.grid(row=7,column=0,columnspan=3,padx=10,pady=10)

result = Label(root, text = 'Resultado:', font=('calibre',10, 'bold')) 
result.grid(row=8,column=0,padx=10,pady=10,sticky=E)


resultado = Entry(root,width=35,borderwidth=5)
resultado.grid(row=8,column=1,columnspan=1,padx=10,pady=10)

root.mainloop()