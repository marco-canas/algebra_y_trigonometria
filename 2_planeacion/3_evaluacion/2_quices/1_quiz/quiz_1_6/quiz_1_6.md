




Aquí tienes un **diseño detallado de un quiz estructurado para Jupyter Notebook** con **autoevaluación en Python (SymPy)**, ideal para **un aula invertida**, enfocado en los temas 1.1 a 1.4 del Swokowski (13.ª ed.). Cada pregunta exige que los estudiantes **justifiquen sus procedimientos** usando expresamente las definiciones y propiedades de los números reales tal como las presenta el texto.

---

## Estructura sugerida del Notebook

1. **Portada e instrucciones**
2. **Configuración inicial** (librerías, símbolos)
3. **Cuatro secciones de preguntas**, cada una con:

   * Enunciado en celdas Markdown, solicitando justificación teórica
   * Celda de código con plantilla para respuesta y autoevaluación (`assert`)
4. **Instrucciones de entrega final**

---

## Encabezado y configuración

```python
# =====================================================
# Quiz interactivo: Álgebra – Swokowski, 13.ª edición
# Temas: 1.1–1.4 — Números reales, exponentes, expresiones
# Integración con aula invertida — Justificación requerida
# =====================================================

import sympy as sp
sp.init_printing()
x, y = sp.symbols('x y')
```

---

## Pregunta 1 – Números reales (5 puntos)

```markdown
**1a) Clasificación:** Determina si cada uno de los siguientes números es natural, entero, racional, irracional o real:
\[
-7,\quad \frac{22}{7},\quad \sqrt{3},\quad 0.\overline{45}
\]
**Justificación:** Cita la definición de racional (como “un número que se puede expresar como a/b con a, b enteros y b ≠ 0”) y explica qué significa pertenecer a cada conjunto.

**1b) Propiedad de cierre:** Demuestra que los números reales son cerrados bajo la multiplicación. Proporciona un ejemplo con números racionales y otro con irracionales, citando la propiedad de cierre en el texto.
```

```python
nums = [-7, sp.Rational(22, 7), sp.sqrt(3), sp.Rational(5, 11)]
for n in nums:
    print(f"{n}: racional: {n.is_rational}, irracional: {n.is_irrational}")

# Ejemplos de cierre
a = sp.Rational(3, 5)
b = sp.sqrt(2)
prod1, prod2 = a * sp.Rational(7, 4), b * sp.sqrt(3)
assert prod1.is_real and prod2.is_real, "Propiedad de cierre bajo multiplicación falló"
print("Productos reales:", prod1, prod2)
```

---

## Pregunta 2 – Exponentes y radicales (5 puntos)

```markdown
**2a) Simplificación:** Simplifica \(\sqrt{48} - 2\sqrt{12}\), usando propiedades de radicales como \(\sqrt{ab} = \sqrt{a}\cdot\sqrt{b}\). Justifica cada paso.

**2b) Reescritura:** Escribe \( x^{-\tfrac{5}{3}} \cdot y^{\tfrac{1}{2}} \) usando únicamente exponentes positivos y radicales. Explica la ley de exponentes negativos y cómo esto está fundamentado en la teoría de potencias de los reales.
```

```python
expr2a = sp.sqrt(48) - 2 * sp.sqrt(12)
res2a = sp.simplify(expr2a)
assert res2a == 2 * sp.sqrt(3), "Error en simplificación"
print("Resultado 2a:", res2a)

expr2b = x**(-sp.Rational(5, 3)) * y**(sp.Rational(1, 2))
res2b = 1 / (x**(sp.Rational(5, 3))) * sp.sqrt(y)
print("Resultado 2b:", res2b)
```

---

## Pregunta 3 – Expresiones algebraicas (5 puntos)

```markdown
**3a) Expansión:** Expande y simplifica \((3x - 2)^2\), fundamentando el uso de la propiedad distributiva y el binomio cuadrado.

**3b) Simplificación algebraica:** Simplifica \(\frac{4x^3 - 8x^2}{4x}\), citando la propiedad de cancelación de potencias (\(x^a / x^b = x^{a-b}\)) y mencionando la condición \(x \neq 0\).
```

```python
expr3a = (3*x - 2)**2
res3a = sp.expand(expr3a)
assert res3a == 9*x**2 - 12*x + 4, "Expansión incorrecta"
print("Resultado 3a:", res3a)

expr3b = (4*x**3 - 8*x**2) / (4*x)
res3b = sp.simplify(expr3b)
assert res3b == x**2 - 2*x, "Simplificación incorrecta"
print("Resultado 3b:", res3b, "| Restricción: x ≠ 0")
```

---

## Pregunta 4 – Expresiones fraccionarias (5 puntos)

```markdown
**4a) Simplificación fraccionaria:** Simplifica la expresión \(\frac{x^2 - 4}{x^2 + 3x + 2}\). Factoriza, cancela términos y menciona las restricciones \(x \neq -1, x \neq -2\).

**4b) Suma de fracciones:** Calcula \(\frac{3}{x-1} + \frac{2}{x+2}\), encuentra el denominador común, suma y simplifica. Justifica la propiedad de cierre en la suma de fracciones reales.
```

```python
expr4a = (x**2 - 4) / (x**2 + 3*x + 2)
res4a = sp.simplify(expr4a)
assert res4a == (x - 2) / (x + 1), "Error en simplificación"
print("Resultado 4a:", res4a, "| Restricciones: x ≠ -1, -2")

expr4b = 3/(x-1) + 2/(x+2)
res4b = sp.simplify(expr4b)
print("Resultado 4b:", res4b)
```

---

## Instrucciones de entrega

```markdown
**Entrega final:**
- Asegúrate de añadir en cada pregunta las **justificaciones teóricas** en celdas Markdown, citando definiciones y propiedades del texto.
- Guarda el archivo como `quiz_swokowski.ipynb`.
- Sube tu trabajo a tu repositorio personal según el modelo del curso.
```

---

## Ventajas de este formato

* **Feedback inmediato** con `assert`, ayudando a autoevaluarse.
* Refuerza la conexión entre la **teoría formal (propiedades de los reales)** y la **práctica simbólica computacional**.
* Facilita la integración con **metodologías activas**, como el aula invertida.

¿Te gustaría que también prepare una versión con retroalimentación más visual o dinámica, por ejemplo empleando `ipywidgets` para mostrar correcciones paso a paso o pistas interactivas?
