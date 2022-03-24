# -*- coding: utf-8 -*-
"""
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib import pyplot
import sys

op = 0;

def menuGraficas(op):
    print("Menu de graficas de matematicas")
    print("1. Curva Normal con media 0 y varianza 1")
    print("2. Curva de Agnesis")
    print("3. Folio de Descartes")
    print("4. Lemniscata de Bernoulli")
    print("5. Curva de Proa")
    print("6. Creditos")
    print("7. Salir")
    op = int(input("Opcion: "))
    
    opciones(op)

def opciones(op):    
    if op == 1:
        
        
        domain = np.linspace(-1,1,1000)
        plt.plot(domain,norm.pdf(domain, 0))
        plt.title("Standard Normal")
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.show()
        menuGraficas(op)
    
    
    
    elif op == 2:
        
        a = 2
        
        def f(x):
            return (8 * a) / (pow(x,2) + pow(a,2))
        
        
        x = range(-10, 10)
        
        pyplot.plot(x, [f(i) for i in x])
        
        #Establecemos el color de los ejes.
        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        
        #Especificamos los limites de los ejes.
        pyplot.xlim(-8, 8)
        pyplot.ylim(-8, 8)
        
    
        
        # Mostramos el gráfico.
        pyplot.show()
        menuGraficas(op)
    
    elif op == 3:
        
        a = 2
        t = np.linspace(0, 2 * np.pi, 1000)
        r = (3 * a * np.sin(t) * np.cos(t)) / (pow(np.sin(t), 3) + pow(np.cos(t), 3))
    
        # Transformación de coordenadas polares a coordenadas cartesianas
        x, y = r * np.cos(t), r * np.sin(t)
    
        fig: plt.Figure = plt.figure()
    
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
    
        ax = fig.add_subplot()
        ax.plot(x, y, color="#ffb6c1",linewidth=2)
    
        # Estilización de la gráfica
        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    
        plt.show()
        menuGraficas(op)
    
       
    elif op == 4:
        t = np.linspace(0, 2*np.pi, num=1000)
    
        a = 1
    
        x = a * np.cos(t) / (np.sin(t)**2 + 1)
        y = a * np.cos(t) * np.sin(t) / (np.sin(t)**2 + 1)
        
        
        
        plt.plot(x,y)
        plt.show() 
        menuGraficas(op)
    
    elif op == 5:
        a = 6

        t = np.linspace(0, 2 * np.pi, 1000)
        r = (pow(np.cos(t),2) * a * np.sin(t) - pow(np.sin(t),3) /  pow(np.cos(t),4) )

           # Transformación de coordenadas polares a coordenadas cartesianas
        x, y = r * np.cos(t), r * np.sin(t)

        fig: plt.Figure = plt.figure()

        xmin, xmax, ymin, ymax = -5, 5, -5, 5

        ax = fig.add_subplot()
        ax.plot(x, y, color="green",linewidth=2)

           # Estilización de la gráfica
        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()
        menuGraficas(op)
        
    elif op == 6:
        print("Hecho por el Team LeJeRoHub development\n")
        print("Jezer Mejia Otero")
        print("Leo Corea Navarrete")
        print("Roire Villacencio Obregon")
        print("Matematica discreta\n\n")
        menuGraficas(op)
        
    elif op == 7:
        print("Gracias por usar\n")
        sys.exit()
    
        
    elif (op <= 0) or (op >= 7):
        print("\nOpcion no valida\n\n")
        
        menuGraficas(op)
        
        
print (menuGraficas(op))


