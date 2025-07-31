# Este script es para que el estudiante pueda estudiar a la función sinosoidal 
# desde la terminal cmd cambiando los parámetros A, B, C y D de manera manual 

import numpy as np
import matplotlib.pyplot as plt

def graficar_seno(A=1, B=1, C=0, D=0):
    x = np.linspace(0, 4*np.pi, 200)
    y = A * np.sin(B*x + C) + D
    plt.figure(figsize=(8, 3))
    plt.plot(x, y, color='red')
    plt.grid()
    plt.show()

while True:
    A = float(input("Amplitud (A): "))
    B = float(input("Periodo (B): "))
    C = float(input("Fase (C): "))       # desplazamiento horizontal 
    D = float(input("Sesgo (D): "))      # desplazamiento vertical 
    graficar_seno(A, B, C, D)
    if input("¿Continuar? (s/n): ").lower() != 's':
        break