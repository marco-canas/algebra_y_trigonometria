# Prompt para el diseño de quices 

Dame un diseño de un quiz para evaluar, en cuatro ítem, los temas: 
   1.1 Números reales,  
   1.2 Exponentes y radicales,  
   1.3 Expresiones algebraicas. 
   1.4 Expresiones Fraccionarias. 
del texto de "Álgebra y trigonometría de Swokowski" treceava edición que se puede descargar gratis de: https://archive.org/details/algebra-y-trigonometria-con-geometria-analitica-13va-edicion-earl-w.-swokowski/page/n3/mode/2up. Este diseño es para un curso de Álgebra y Trigonometría cuyo plan es el que está en esta url: https://github.com/marco-canas/algebra_y_trigonometria/blob/main/1_plan_curso/1_programa_algebra_and_trigonometry.md. Pero pide en cada uno de los cuatro puntos del quiz, el que el estudiante justifique sus procedimientos utilizando las definiciones y propiedades de los números reales dada por Swokowski. Diseña cada item de tal manera que el primer punto sea teórico de verdadero o falso con justificación, donde la justificación valga la mitad del valor de cada pregunta. Y el último de los cuatro item, evalúe a partir de un problema de aplicación dado por un enunciado verbal. Y los item 2 y 3 sean de ejercitación, donde en cada item se evaluen la mayor cantidad posible de los conocimientos en cuanto a definiciones y propiedades algebraicas de los números reales.    


**diseño de quiz** alineado tanto con los temas 1.1, 1.2 y 1.3 del *Swokowski 13a ed.* como con el plan de curso que tenemos en GitHub.
El formato está pensado para que puedas aplicarlo en aula invertida y ABPP, con equilibrio entre preguntas conceptuales, procedimentales y de aplicación contextual.

---

## **Diseño de Quiz — Álgebra y Trigonometría**

**Temas:**
1.1 Números reales
1.2 Exponentes y radicales
1.3 Expresiones algebraicas

**Duración:** 30 minutos
**Total:** 20 puntos
**Formato:** Preguntas cerradas (opción múltiple y falso/verdadero) y abiertas (resolución y justificación).

---

### **Parte A – Conceptos básicos (6 puntos)**

**1. (1 pt)** Clasifique cada número como natural, entero, racional, irracional o real (Justifique cada una de sus respuestas utilizando la definición, propiedades y ejemplso que considere adecuados):
a) $-5$
b) $\frac{22}{7}$
c) $\sqrt{2}$
d) $0.333\ldots$

**2. (1 pt)** Marque **V** o **F** y justifique cada una de sus respuestas:

* Todo número entero es un número racional.
* Todo número racional es un número entero.
Aquí tienes **9 afirmaciones adicionales** para el punto teórico del quiz, siguiendo la idea de **verdadero o falso con justificación**, todas basadas en definiciones y propiedades de los números reales según Swokowski:

---

**1.** Todo número real tiene una raíz cuadrada que también es un número real.

**2.** El conjunto de los números racionales es cerrado bajo la suma, la resta, la multiplicación y la división (excepto por cero).

**3.** El valor absoluto de un número real siempre es mayor o igual que cero.

**4.** El inverso aditivo de cualquier número real es siempre un número negativo.

**5.** Si $a$ y $b$ son números reales positivos, entonces $\sqrt{a+b} = \sqrt{a} + \sqrt{b}$.

**6.** La multiplicación de números reales es conmutativa y asociativa.

**7.** El producto de dos números reales negativos siempre es un número positivo.

**8.** Todo número real es un número racional o un número irracional, pero no ambos.

**9.** El conjunto de los números enteros es un subconjunto de los números reales y también de los números racionales.

---

Si quieres, puedo **añadir estas 9 afirmaciones al archivo .docx del quiz**, colocándolas como opciones alternativas para el **Ítem 1** para que tengas un banco de preguntas teóricas. ¿Quieres que lo haga?



**3. (2 pts)** Simplifique:

$$
\sqrt{50} + \sqrt{18}
$$

**4. (2 pts)** Escriba la expresión $3x^{-2}y^{\frac{3}{4}}$ usando únicamente exponentes positivos y radicales.

---

### **Parte B – Procedimientos (8 puntos)**

**5. (2 pts)** Simplifique completamente:

$$
\frac{2x^{\frac{3}{2}}y^{-2}}{4x^{\frac{1}{2}}y^{-5}}
$$

**6. (2 pts)** Efectúe y simplifique:

$$
(3x - 2y)^2 - (x + y)^2
$$

**7. (2 pts)** Exprese en forma de un único radical:

$$
\sqrt[3]{8x^5} \cdot \sqrt[3]{4x}
$$

**8. (2 pts)** Evalúe $\left( 16^{\frac{3}{4}} \right)$ y exprese el resultado como entero o fracción.

---

### **Parte C – Aplicación contextual (6 puntos)**

**9. (3 pts)** Un cuadrado tiene área:

$$
A = (5x^{\frac{1}{2}} - 2)^2
$$

Expanda la expresión y simplifique para expresar el área únicamente como suma/resta de términos.

**10. (3 pts)** En física, la ecuación de velocidad final bajo aceleración constante es:

$$
v_f = \sqrt{v_i^2 + 2a d}
$$

Si $v_i = 4 \, \text{m/s}$, $a = 3 \, \text{m/s}^2$ y $d = 6 \, \text{m}$, calcule $v_f$ y exprese el resultado en forma simplificada.

---

### **Criterios de calificación**

* Procedimiento correcto y ordenado: 50%
* Respuesta final correcta: 40%
* Notación matemática adecuada: 10%

---  

# Versión del primer quiz utilizando SymPy y NumPy. 

Si quieres, puedo también prepararte la **versión en Jupyter Notebook** del quiz para que tus estudiantes lo puedan resolver en Python usando `SymPy` y `NumPy`, y así reforzar la conexión con el aula invertida y la computación simbólica.
¿Quieres que te la genere ahora?  

Perfecto, Marco.
Aquí tienes el **quiz en formato Jupyter Notebook**, listo para que tus estudiantes lo resuelvan usando **SymPy** y **NumPy**, siguiendo el mismo diseño que te propuse antes.

Incluye celdas Markdown con los enunciados y celdas de código con plantillas para que ellos completen la solución.

---

```python
# ===========================================
# QUIZ - Álgebra y Trigonometría con Python
# Temas:
# 1.1 Números reales
# 1.2 Exponentes y radicales
# 1.3 Expresiones algebraicas
# ===========================================

import sympy as sp
import numpy as np

# Configuración para que las expresiones se vean bonitas
sp.init_printing()
```

```markdown
# **Parte A – Conceptos básicos (6 puntos)**

## 1. (1 pt) Clasifique cada número como natural, entero, racional, irracional o real:
a) -5  
b) 22/7  
c) sqrt(2)  
d) 0.333...

Usa SymPy para verificar si cada número pertenece a cada conjunto.
```

```python
# Ejemplo para verificar pertenencia a un conjunto numérico
nums = [-5, sp.Rational(22,7), sp.sqrt(2), sp.Rational(1,3)]

for n in nums:
    print(f"Número: {n}")
    print("Es entero:", sp.Integer(n) == n if n.is_real else False)
    print("Es racional:", n.is_rational)
    print("Es irracional:", n.is_irrational)
    print("Es real:", n.is_real)
    print()
```

```markdown
## 2. (1 pt) Marque V o F:
- Todo número entero es un número racional.  
- Todo número racional es un número entero.
```

```python
# Usar ejemplos para justificar
n1 = sp.Integer(-5)   # entero
n2 = sp.Rational(3,4) # racional no entero

print("Todo entero es racional:", n1.is_rational)
print("Todo racional es entero:", n2.is_integer)
```

```markdown
## 3. (2 pts) Simplifique:
\[
\sqrt{50} + \sqrt{18}
\]
```

```python
expr3 = sp.sqrt(50) + sp.sqrt(18)
expr3_simpl = sp.simplify(expr3)
expr3_simpl
```

```markdown
## 4. (2 pts) Exprese \( 3x^{-2}y^{3/4} \) usando únicamente exponentes positivos y radicales.
```

```python
x, y = sp.symbols('x y', positive=True)
expr4 = 3*x**(-2)*y**(sp.Rational(3,4))
expr4_rewritten = sp.simplify(expr4)
expr4_positive_exp = sp.powdenest(expr4, force=True)
expr4, expr4_positive_exp
```

---

```markdown
# **Parte B – Procedimientos (8 puntos)**

## 5. (2 pts) Simplifique completamente:
\[
\frac{2x^{3/2}y^{-2}}{4x^{1/2}y^{-5}}
\]
```

```python
expr5 = (2*x**(sp.Rational(3,2))*y**(-2)) / (4*x**(sp.Rational(1,2))*y**(-5))
sp.simplify(expr5)
```

```markdown
## 6. (2 pts) Efectúe y simplifique:
\[
(3x - 2y)^2 - (x + y)^2
\]
```

```python
expr6 = (3*x - 2*y)**2 - (x + y)**2
sp.expand(expr6)
```

```markdown
## 7. (2 pts) Exprese en forma de un único radical:
\[
\sqrt[3]{8x^5} \cdot \sqrt[3]{4x}
\]
```

```python
expr7 = (8*x**5)**(sp.Rational(1,3)) * (4*x)**(sp.Rational(1,3))
sp.simplify(expr7)
```

```markdown
## 8. (2 pts) Evalúe \( 16^{3/4} \) y exprese el resultado como entero o fracción.
```

```python
expr8 = 16**(sp.Rational(3,4))
sp.nsimplify(expr8)
```

---

```markdown
# **Parte C – Aplicación contextual (6 puntos)**

## 9. (3 pts) Un cuadrado tiene área:
\[
A = (5x^{1/2} - 2)^2
\]
Expanda y simplifique.
```

```python
expr9 = (5*x**(sp.Rational(1,2)) - 2)**2
sp.expand(expr9)
```

```markdown
## 10. (3 pts) Ecuación de velocidad final:
\[
v_f = \sqrt{v_i^2 + 2ad}
\]
Con:
\( v_i = 4 \, m/s \), \( a = 3 \, m/s^2 \), \( d = 6 \, m \)
```

```python
v_i, a, d = 4, 3, 6
v_f = np.sqrt(v_i**2 + 2*a*d)
v_f
```

---

💡 **Sugerencia para el aula invertida:**
Puedes pedir que los estudiantes suban el notebook resuelto a su repositorio personal de GitHub, con capturas de pantalla de las salidas y explicaciones escritas en las celdas Markdown.

```

---

Si quieres, puedo también prepararte **una versión autocorregible** del quiz en Jupyter usando `assert` o `pytest` para que los estudiantes reciban retroalimentación automática.  
¿Quieres que la haga así también?
```

