



¡Claro! Aquí tienes una propuesta detallada para el **quiz en formato Jupyter Notebook** con **autoevaluación en SymPy y NumPy**, pensada para un enfoque de aula invertida. El cuaderno permitirá a tus estudiantes resolver los ejercicios de los temas 1.1 a 1.4 (Números reales, exponentes y radicales, expresiones algebraicas, expresiones fraccionarias) usando Python, y **justificar sus pasos** mediante comentarios.

---

## Diseño del Jupyter Notebook: Quiz con Autoevaluación

### Estructura del notebook

1. **Encabezado** – Introducción del propósito y temas.
2. **Configuración** – Carga de librerías (`sympy`, `numpy`) y variables simbólicas.
3. **Preguntas** – Cada una sigue esta estructura:

   * Enunciado en celda Markdown.
   * Código plantilla en celda siguiente para que el estudiante rellene.
   * Evaluación automática usando `assert` y feedback.
4. **Instrucciones finales** – Cómo entregar / versión GitHub.

---

### Esqueleto del Notebook

```python
# ===============================================
# Quiz Automático: Álgebra – Swokowski, 13ª ed.
# Temas: 1.1 a 1.4 – Con justificación usando propiedades
# Autor: Marco Cañas
# Uso: Aula invertida con Python (SymPy, NumPy)
# ===============================================

import sympy as sp
import numpy as np

sp.init_printing()

# Variables simbólicas que usaremos repetidamente
x, y = sp.symbols('x y')
```

---

### Pregunta 1 – Números reales (5 pts)

```markdown
**1a)** Clasifica: \(-7,\;\tfrac{22}{7},\;\sqrt{3},\;0.\overline{45}\).  
Justifica cada clasificación citando la definición de número racional (como “un número que se puede expresar como a/b, con a,b enteros, b≠0”).

**1b)** Demuestra que los reales son cerrados bajo multiplicación. Usa un ejemplo con racionales y otro con irracionales, y comenta cómo aplica la propiedad de cierre (“si a y b son reales, entonces a·b es real”).
```

```python
# Ejemplo plantilla
nums = [-7, sp.Rational(22,7), sp.sqrt(3), sp.Rational(5,11)]  # 0.45… sería un racional repetido
for n in nums:
    print(n, "→ racional?", n.is_rational, "| irracional?", n.is_irrational)
# Ejemplo de cierre
a = sp.Rational(3,4)
b = sp.sqrt(2)
prod1 = a * sp.Rational(7,5)
prod2 = b * sp.sqrt(3)
assert prod1.is_real and prod2.is_real, "Error: no hay cierre bajo multiplicación"
print("Cierre verificado – productos son reales:", prod1, prod2)
```

---

### Pregunta 2 – Exponentes y radicales (5 pts)

```markdown
**2a)** Simplifica: \(\sqrt{48} - 2\sqrt{12}\). Justifica con propiedades de radicales (por ejemplo, \(\sqrt{ab} = \sqrt{a}\cdot\sqrt{b}\)).

**2b)** Reescribe \( x^{-5/3}\,y^{1/2} \) usando sólo exponentes positivos y radicales, mencionando la regla \(a^{-m} = 1/a^m\).
```

```python
expr2a = sp.sqrt(48) - 2*sp.sqrt(12)
res2a = sp.simplify(expr2a)
assert res2a == 2*sp.sqrt(3), "Simplificación incorrecta"
print("Resultado 2a:", res2a)

expr2b = x**(-sp.Rational(5,3)) * y**(sp.Rational(1,2))
res2b = 1/(x**(sp.Rational(5,3))) * sp.sqrt(y)
print("Resultado 2b:", res2b)
```

---

### Pregunta 3 – Expresiones algebraicas (5 pts)

```markdown
**3a)** Expande y simplifica: \((3x - 2)^2\). Explica la propiedad distributiva usada.

**3b)** Simplifica: \(\frac{4x^3 - 8x^2}{4x}\). Justifica usando factorización, cancelación, y propiedad de cociente (\(x^a/x^b = x^{a-b}\)), mencionando restricciones si \(x=0\).
```

```python
expr3a = (3*x - 2)**2
res3a = sp.expand(expr3a)
assert res3a == 9*x**2 - 12*x + 4, "Error en expansión"
print("Resultado 3a:", res3a)

expr3b = (4*x**3 - 8*x**2)/(4*x)
res3b = sp.simplify(expr3b)
assert res3b == x**2 - 2*x, "Error en simplificación"
print("Resultado 3b:", res3b, "| nota: x ≠ 0")
```

---

### Pregunta 4 – Expresiones fraccionarias (5 pts)

```markdown
**4a)** Simplifica: \(\frac{x^2 - 4}{x^2 + 3x + 2}\). Factoriza, cancela y menciona condiciones (\(x ≠ -1, -2\)).

**4b)** Suma: \(\frac{3}{x-1} + \frac{2}{x+2}\). Encuentra el común denominador, simplifica y aplica la propiedad de cierre en los reales.
```

```python
expr4a = (x**2 - 4)/(x**2 + 3*x + 2)
res4a = sp.simplify(expr4a)
assert res4a == (x - 2)/(x + 1), "Error en simplificación"
print("Resultado 4a:", res4a, "| restricciones: x ≠ -1, -2")

expr4b = 3/(x-1) + 2/(x+2)
res4b = sp.simplify(expr4b)
print("Resultado 4b:", res4b)
```

---

### Instrucciones para entrega

```markdown
### ¡Listo para entregar!
- Asegúrate de conservar las celdas con justificación en comentarios Markdown.
- Guarda el archivo como `quiz_swokowski.ipynb`.
- Súbelo a tu repositorio personal en GitHub conforme al plan de aula invertida.
```

---

## Integración al aula invertida

* El cuaderno permite **auto-evaluación inmediata** gracias a los `assert`.
* Favorece la documentación de justificaciones teóricas junto al código.
* Refuerza la conexión entre teoría (propiedades de los números reales) y práctica computacional.

¿Te gustaría que prepare también una versión con retroalimentación más detallada, usando por ejemplo `ipywidgets` o funciones personalizadas para comentarios más enriquecidos?
