# Prompt 

Dame un diseño de un quiz para evaluar los temas: 
   1.1 Números reales,  
   1.2 Exponentes y radicales,  
   1.3 Expresiones algebraicas. 
   1.4 Expresiones Fraccionarias. 
del texto de "Álgebra y trigonometría de Swokowski" treceava edición que se puede descargar gratis de: https://archive.org/details/algebra-y-trigonometria-con-geometria-analitica-13va-edicion-earl-w.-swokowski/page/n3/mode/2up. Este diseño es para un curso de Álgebra y Trigonometría cuyo plan es el que está en esta url: https://github.com/marco-canas/algebra_y_trigonometria/blob/main/1_plan_curso/1_programa_algebra_and_trigonometry.md. Pero pide en cada uno de los cuatro puntos del quiz, el que el estudiante justifique sus procedimientos utilizando las definiciones y propiedades de los números reales dada por Swokowski.   

Aquí tienes un **diseño de quiz** que incorpora los temas 1.1 a 1.4 del libro *Álgebra y Trigonometría con Geometría Analítica* (13.ª edición, Swokowski y Cole) y exige que los estudiantes **justifiquen cada procedimiento usando las definiciones y propiedades de los números reales** presentadas en el texto ([demo.webassign.net][1], [Studocu][2]).

---

## Diseño de Quiz – Fundamentos de Álgebra (Swokowski, 13.ª edición)

**Temas cubiertos:**
1.1 Números reales
1.2 Exponentes y radicales
1.3 Expresiones algebraicas
1.4 Expresiones fraccionarias

**Duración:** 45 minutos
**Valor total:** 20 puntos

**Formato:**
Preguntas de respuesta abierta (resolución y justificación detallada), donde el estudiante debe **citar y aplicar** explícitamente las propiedades y definiciones del texto —por ejemplo, cierre, conmutatividad, identidad, inversos, distributividad, reglas de exponentes, simplificación de fracciones, etc.— para respaldar cada paso.

---

### **Parte 1 – Números reales (5 puntos)**

**1. (2 pts)** Clasifica cada número y justifica:

* $-\frac{7}{3}$
* $\sqrt{5}$

*Justificación esperada:* Indicar si cada número es entero, racional o irracional, y usar definiciones como: “un número racional es aquel que puede expresarse como $\frac{a}{b}$ con $a, b$ enteros y $b \neq 0$”; luego, para irracional, referirse a la imposibilidad de representarse así ([Studocu][2]).

**2. (3 pts)** Explica qué significa que los números reales son cerrados bajo adición y multiplicación. Muestra que los números irracionales no son cerrados bajo suma ni bajo multiplicación, muéstralo con ejemplos numéricos y justifica claramente.

*Justificación esperada:* Citar la propiedad de cierre, y realizar ejemplos como la suma de un racional con un irracional es real, o el producto de irracionales.   

---

### **Parte 2 – Exponentes y radicales (5 puntos)**

**3. (2 pts)** Simplifica $\sqrt{72} - \sqrt{18}$. Justifica cada paso con propiedades de los radicales y exponentes.

*Justificación esperada:* Uso de propiedades como $\sqrt{a b} = \sqrt{a} \cdot \sqrt{b}$, extracción de factores cuadrados, etc., citando el tratado del texto sobre exponentes y radicales ([demo.webassign.net][1]).

**4. (3 pts)** Reescribe $x^{-\frac{3}{2}} \cdot y^2$ usando exponentes positivos y radicales. Explica el uso de reglas de exponentes aplicadas.

*Justificación esperada:* Mostrar que $x^{-\frac{3}{2}} = \frac{1}{x^{3/2}} = \frac{1}{(\sqrt{x})^3}$, explicando la ley de exponentes negativos y de fracciones ([demo.webassign.net][1]).

---

### **Parte 3 – Expresiones algebraicas (5 puntos)**

**5. (2 pts)** Expande y simplifica $(2x - 3)^2$. Luego justifica el uso de la propiedad distributiva y las propiedades de orden en la simplificación.

*Justificación esperada:* Aplicar la fórmula $(a - b)^2 = a^2 - 2ab + b^2$, citando la propiedad distributiva y las reglas de los números reales ([Studocu][2]).

**6. (3 pts)** Simplifica la expresión:

$$
\frac{3x^3 + 6x^2}{3x}
$$

Explica cómo se aplica la propiedad de cocientes y la cancelación de factores en números reales.

*Justificación esperada:* Mostrar la factorización y cancelación (división término a término), respaldado por la propiedad de los cocientes del texto ([Studocu][2]).

---

### **Parte 4 – Expresiones fraccionarias (5 puntos)**

**7. (2 pts)** Simplifica completamente:

$$
\frac{x^2 - 9}{x^2 - 6x + 9}
$$

Incluye justificación con factorización, cancelación de factores, y condiciones de validez (denominador ≠ 0).

*Justificación esperada:* Factorizar (diferencia de cuadrados y trinomio cuadrado perfecto), cancelar y especificar restricciones; citar las propiedades de los cocientes y fracciones del texto ([Studocu][2]).

**8. (3 pts)** Suma y simplifica:

$$
\frac{2}{x+1} + \frac{3}{x-1}
$$

Explica el proceso de encontrar el mínimo común denominador (mcd) y aplicar propiedades de adición sobre fracciones reales.

*Justificación esperada:* Mostrar paso a paso la obtención del denominador común, la suma, y la simplificación final; usando las propiedades de los cocientes vistas en el texto ([Studocu][2]).

---

### **Resumen de puntuación**

| Parte     | Tema                      | Puntos |
| --------- | ------------------------- | ------ |
| 1         | Números reales            | 5      |
| 2         | Exponentes y radicales    | 5      |
| 3         | Expresiones algebraicas   | 5      |
| 4         | Expresiones fraccionarias | 5      |
| **Total** |                           | **20** |

---

### **Instrucciones para estudiantes**

* Presenta cada resolución en detalle, indicando claramente **qué propiedad o definición** estás usando (por ejemplo: “Por la propiedad distributiva…, por cierre de los reales…, etc.”).
* Si corresponde, señala restricciones (como $x \neq \dots$).
* Sé riguroso con la notación y el orden lógico.
* Esta actividad busca tanto tu habilidad para manipular expresiones como tu comprensión de por qué cada paso es válido dentro del marco teórico del texto.

---

¿Te gustaría que además te proporcione esta versión en un *Jupyter Notebook* o con **autoevaluación en SymPy** para integración con el aula invertida?



