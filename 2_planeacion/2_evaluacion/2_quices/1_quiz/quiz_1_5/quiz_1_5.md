




Aquí tienes un diseño de **quiz en formato *Jupyter Notebook*** con **autoevaluación en SymPy y NumPy**, pensado para tu curso de Álgebra y Trigonometría basado en Swokowski (13ª edición) y alineado con los temas 1.1 a 1.4. Cada sección exige justificación explícita usando las **definiciones y propiedades de los números reales** según el texto.

---

## Estructura del Notebook

1. **Encabezado** — presentación del quiz y directrices para la justificación.
2. **Configuración inicial** — importación de librerías, variables simbólicas.
3. **Secciones del Quiz** — cuatro preguntas, cada una con:

   * Enunciado (Markdown) con exigencia de justificación.
   * Celda de código con plantilla para completar y autoevaluación (`assert`).
4. **Instrucciones de entrega**.

---

## Contenido

```python
# ================================
# Quiz Automático: Swokowski, 13° ed.
# Temas 1.1–1.4: Con justificación teórica
# Área: Álgebra y Trigonometría
# Formato: Jupyter Notebook con autoevaluación
# ================================

import sympy as sp
import numpy as np

sp.init_printing()
x, y = sp.symbols('x y')
```

---

### 1. Números reales (5 pts)

```markdown
**Pregunta 1a)** Clasifica: \(-7,\; \tfrac{22}{7},\; \sqrt{3},\; 0.\overline{45}\).  
Justifica usando definiciones del texto (como “un número racional es aquel que puede expresarse como a/b con a, b enteros y b≠0”) y menciona la propiedad de cierre bajo suma o multiplicación.

**Pregunta 1b)** Demuestra que los reales son cerrados bajo multiplicación, con un ejemplo racional y otro irracional.
```

```python
nums = [-7, sp.Rational(22,7), sp.sqrt(3), sp.Rational(5,11)]
for n in nums:
    print(n, "→ racional?", n.is_rational, "| irracional?", n.is_irrational)

a = sp.Rational(2,3)
b = sp.sqrt(5)
prod1 = a * sp.Rational(7,4)
prod2 = b * sp.sqrt(2)
assert prod1.is_real and prod2.is_real, "Cierre multiplicativo no verificado."
print("Productos son reales:", prod1, prod2)
```

---

### 2. Exponentes y radicales (5 pts)

```markdown
**2a)** Simplifica: \(\sqrt{48} - 2\sqrt{12}\) usando propiedades de radicales.

**2b)** Reescribe \( x^{-5/3} \cdot y^{1/2} \) con exponentes positivos y radicales, explicando la ley de exponentes negativos.
```

```python
expr2a = sp.sqrt(48) - 2*sp.sqrt(12)
res2a = sp.simplify(expr2a)
assert res2a == 2*sp.sqrt(3), "Simplificación incorrecta."
print("Result 2a:", res2a)

expr2b = x**(-sp.Rational(5,3))*y**(sp.Rational(1,2))
res2b = 1/(x**(sp.Rational(5,3))) * sp.sqrt(y)
print("Result 2b:", res2b)
```

---

### 3. Expresiones algebraicas (5 pts)

```markdown
**3a)** Expande y simplifica: \((3x - 2)^2\), fundamentando el uso de distributividad.

**3b)** Simplifica \(\frac{4x^3 - 8x^2}{4x}\). Justifica mediante factorización, cancelación y propiedades de cocientes, indicando \(x ≠ 0\).
```

```python
expr3a = (3*x - 2)**2
res3a = sp.expand(expr3a)
assert res3a == 9*x**2 - 12*x + 4, "Expansión incorrecta."
print("Result 3a:", res3a)

expr3b = (4*x**3 - 8*x**2)/(4*x)
res3b = sp.simplify(expr3b)
assert res3b == x**2 - 2*x, "Simplificación incorrecta."
print("Result 3b:", res3b, "| Restricción: x ≠ 0")
```

---

### 4. Expresiones fraccionarias (5 pts)

```markdown
**4a)** Simplifica: \(\frac{x^2 - 4}{x^2 + 3x + 2}\), factorizando, cancelando, y mencionando las restricciones \(x ≠ -1, -2\).

**4b)** Calcula \( \frac{3}{x-1} + \frac{2}{x+2} \), encontrando el MCD, simplificando y mencionando la propiedad de cierre en suma de fracciones reales.
```

```python
expr4a = (x**2 - 4)/(x**2 + 3*x + 2)
res4a = sp.simplify(expr4a)
assert res4a == (x - 2)/(x + 1), "Simplificación incorrecta."
print("Result 4a:", res4a, "| Restricciones: x ≠ -1, -2")

expr4b = 3/(x-1) + 2/(x+2)
res4b = sp.simplify(expr4b)
print("Result 4b:", res4b)
```

---

### Instrucciones de entrega

```markdown
**Entrega:**
- Adjunta justificaciones teóricas en Markdown dentro del notebook para cada paso.
- Guarda el archivo como `quiz_swokowski.ipynb`.
- Sube a tu repositorio según el modelo de aula invertida.
```

---

## Ventajas del Formato

* **Autoevaluación inmediata** con `assert` para feedback claro.
* **Integración teoría–práctica**, reforzando las propiedades formales del texto.
* Ideal para el **aprendizaje invertido**, fomentando reflexión y escritura matemática.

¿Deseas que también prepare una versión con retroalimentación enriquecida (por ejemplo, usando `ipywidgets` o funciones que expliquen errores)?
