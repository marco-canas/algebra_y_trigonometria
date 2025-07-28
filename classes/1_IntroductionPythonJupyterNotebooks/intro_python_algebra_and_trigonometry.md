# Prompt para el diseño del la Introducción a python para el Curso de algebra and trigonometry  

Dame un diseño de primera clase o sesión para este curso para dar una introducción al Lenguaje Python para este curso de "álgebra y trigonometría". Pero que esta introducción esté de acuerdo con el programa anterior del curso dado por el Instituto de matemáticas de la Universidad de Antioquia cuyo nombre de archivo era "0303001_algebra_trigonometry.pdf". Esta introducción al Lenguaje Python pretende formar a los futuros matemáticos en cuanto a los aspectos y habilidades que este lenguaje le provee al matemático según el perfil que el Instituto de matemáticas busca y según el conocimiento en ciencia de datos con técnicas de Machine Learning y Deep Learning debe tener el futuro matemático. Los fines y la misión del programa de matemáticas de mi Universidad de Antioquia lo encuentras en: https://www.matematicasudea.co/matematicas.html


### **Diseño de la Primera Clase: Introducción a Python para Matemáticos**  
**Curso:** Álgebra y Trigonometría (Código: 0303001)  
**Modalidad:** Aula Invertida + Enfoque STEAMS/ABPP  
**Duración:** 2 horas (presencial) + 1 hora de trabajo autónomo (pre-clase)  
**Objetivo:**  
Introducir Python como herramienta fundamental para el matemático, vinculando sus capacidades (cálculo simbólico, visualización, ciencia de datos) con los perfiles de formación del Instituto de Matemáticas de la UdeA: *razonamiento abstracto, modelamiento y aplicaciones en inteligencia artificial*.  

---

### **Pre-Clase (Trabajo Autónomo - 1 hora)**  
**Recursos:**  
1. Video corto (15 min): *"¿Por qué Python en matemáticas?"* (Enlace en Moodle).  
   - Contenido:  
     - Ejemplos de aplicaciones en álgebra (SymPy), trigonometría (Matplotlib) y machine learning (SciKit-Learn).  
     - Testimonios de egresados del Instituto que usan Python en ciencia de datos.  
2. Lectura: [*"Python para Matemáticos"*](https://www.matematicasudea.co/matematicas.html) (Sección "Perfil del Egresado").  
3. Instalación guiada de Anaconda/Jupyter Notebook (documento paso a paso).  

---

### **Sesión Presencial (2 horas)**  

#### **1. Motivación (30 min)**  
- **Actividad STEAMS:**  
  - Discusión en grupos: *"¿Cómo usará Python en su futuro como matemático?"*  
    - Guiada por preguntas como:  
      - *"¿Cómo modelarías un fenómeno periódico (ej: mareas) con trigonometría y Python?"*  
      - *"¿Qué ventajas tiene Python sobre calculadoras tradicionales en álgebra?"*  
  - Presentación de casos reales:  
    - Uso de Python en *machine learning* para predicción de series temporales (relación con progresiones aritméticas/geométricas).  
    - Proyectos de egresados del Instituto en empresas de *data science*.  

#### **2. Fundamentos Prácticos (45 min)**  
- **Demo interactiva (TRRS - Teoría de Registros de Representación):**  
  - **Problema:** *"Graficar la función \( f(x) = x^2 - 4x + 3 \) y encontrar sus raíces"*.  
    - Representación simbólica (SymPy):  
      ```python
      from sympy import symbols, solve, plot
      x = symbols('x')
      f = x**2 - 4*x + 3
      roots = solve(f, x)  # Output: [1, 3]
      ```  
    - Representación gráfica (Matplotlib):  
      ```python
      import matplotlib.pyplot as plt
      import numpy as np
      x_vals = np.linspace(0, 4, 100)
      y_vals = x_vals**2 - 4*x_vals + 3
      plt.plot(x_vals, y_vals)
      plt.scatter(roots, [0, 0], color='red')  # Raíces
      ```  
  - **Reflexión:** Comparar con métodos algebraicos tradicionales (factorización).  

- **Ejercicio guiado (ABP - Aprendizaje Basado en Problemas):**  
  - *"Calcular el ángulo óptimo para un puente usando trigonometría y Python"*.  
    - Uso de `math.radians()` y `math.tan()`.  

#### **3. Conexión con el Perfil del Instituto (30 min)**  
- **Panel:** *"Python en la Ciencia de Datos Matemática"* (Video con egresados).  
  - Habilidades clave mencionadas en el [perfil del Instituto](https://www.matematicasudea.co/matematicas.html):  
    - *"Capacidad para modelar problemas complejos"* → Uso de Pandas para análisis de datos.  
    - *"Pensamiento algorítmico"* → Introducción a NumPy para operaciones matriciales (base para deep learning).  
- **Reto rápido:**  
  - Usar Python para verificar una identidad trigonométrica (ej: \( \sin^2(x) + \cos^2(x) = 1 \)) con SymPy.  

#### **4. Cierre (15 min)**  
- **Tarea para la próxima clase (Aula Invertida):**  
  - Subir a Moodle un Jupyter Notebook con:  
    1. Gráfica de una función polinomial.  
    2. Solución simbólica de una ecuación lineal.  
  - Lectura: *"Introducción a NumPy para álgebra lineal"* (en inglés).  
- **Encuesta rápida:**  
  - *"¿Qué aplicación de Python te gustaría explorar en el curso?"* (Opciones: ML, visualización, cálculo simbólico).  

---

### **Evaluación Formativa**  
- **Rúbrica de participación:**  
  - 50%: Contribuciones en la discusión grupal (calidad argumentativa).  
  - 50%: Entrega del Jupyter Notebook (funcionalidad y comentarios en código).  

### **Recursos Adicionales**  
- **Bibliografía:**  
  - [*"Python for Data Analysis"* (Wes McKinney)](https://wesmckinney.com/book/) → Enlace con álgebra matricial.  
  - Documentación de SymPy (ejemplos en inglés).  
- **Herramientas:**  
  - Google Colab para estudiantes sin instalación local.  

---  
**Nota:** Esta sesión alinea el uso de Python con los ejes del Instituto: *rigor matemático, aplicabilidad en data science* y *comunicación científica en inglés*, sentando las bases para proyectos ABPP futuros (ej: predicción de series con Fourier).