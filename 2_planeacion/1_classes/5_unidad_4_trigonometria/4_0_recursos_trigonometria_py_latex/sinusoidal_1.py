import numpy as np # Genera la progresión aritmética para el dominio de graficación. 
import matplotlib.pyplot as plt # Grafica la función y = y(x) en el dominio de graficación.
from ipywidgets import interact # Interactividad o deslizados para mover los parámetros A, B, C, y D 
#definir dominio  
a, b = 0, 4*np.pi
# definir conjunto de llegada
c, d = -6, 6
@interact(A=(1, 5), B = (1, 5), C = (0, 2*np.pi, 0.1), D = (-2, 2))   

def graficar_seno(A=1, B=1, C=0, D=0):
    x = np.linspace(0, 4*np.pi, 200) # crea una secuencia de 201 números entre 0 y 4π 
    y = A * np.sin(B*x + C) + D # 
    plt.figure(figsize=(8, 3)) # genera un lienzo o figura de 10 x 4 pulgadas 
    plt.title('Exploración a las gráficas de $y = A sen(Bx + C) + D$')
    plt.axis([a, b, c, d]) # defines el rectangulo de visualización de la gráfica
    plt.axhline(y = 0, color = 'blue')
    plt.axvline(x = 0)
    plt.xticks(np.arange(a,b+np.pi/2, np.pi/2), ['0', 'pi/2', 'pi', '3pi/2', '2pi', '5pi/2', '6pi/2', '7pi/2', '4pi'] ) # metrizar el eje horizontal o escalar los ejes. 
    plt.yticks(np.arange(c,d+1)) # metrizar el eje vertical 
    plt.plot(x, y, label=f"${A}\\cdot\\sin({B}x + {C:.1f}) + {D}$", color = 'red') # Hace gráficos de líneas 
    plt.legend('Exploración de las gráficas de $y = A \cdot \sin(Bx + C) + D$')
    plt.grid()
    plt.savefig(r"C:\Users\marco\Downloads\exploracion_graficas_y_A_sin.jpg")
    plt.show()

