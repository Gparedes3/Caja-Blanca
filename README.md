# Caja-Blanca — Taller Autónomo de Pruebas de Caja Negra

Clase 2 · Análisis de un sistema de presupuesto con defectos inyectados.

**Equipo:** Guillermo Paredes · Donato Oña · Mateo Villacreses

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `presupuesto_analisis.py` | Código base recibido, **tal como fue entregado** (con sus defectos inyectados, sin corregir) |
| `casos_prueba.md` | Mapa conceptual + plan de pruebas + ejecución dinámica + reportes de defecto |
| `README.md` | Este archivo, con el cierre y la validación conceptual |

## Cómo ejecutar

```bash
python3 presupuesto_analisis.py
```

El script solicita por consola: presupuesto total, número de socios y meses de inversión.

## Resumen de la campaña de pruebas

4 casos diseñados con partición de equivalencia y valores límite · **0 Passed / 4 Failed** ·
4 defectos aislados en las líneas **3–5**, **9** y **12**, más una omisión de validación de dominio.
El detalle completo está en [`casos_prueba.md`](casos_prueba.md).

---

# Cierre y Validación Conceptual de Alta Profundidad

## Desafío Lógico 1

> Según lo investigado en ISTQB, ¿es posible que un Defecto (Bug) exista en el código fuente de
> `presupuesto_analisis.py` durante años sin llegar a causar nunca un Fallo (Failure)?
> Justifiquen técnicamente.

**Sí, es completamente posible, y nuestro propio código lo demuestra.**

La justificación técnica está en la naturaleza de la cadena **Error → Defecto → Fallo**: un **Defecto** es
una condición **estática** que reside en el código y existe desde el instante en que se escribió; un
**Fallo** es un evento **dinámico**, la manifestación observable de ese defecto. Para que el defecto se
convierta en fallo deben cumplirse **tres condiciones simultáneas**:

1. La línea defectuosa debe **ejecutarse** (alcanzabilidad).
2. Debe ejecutarse con un **dato de entrada** que active la condición errónea (infección del estado).
3. El estado corrupto debe **propagarse hasta una salida observable** (propagación).

Si alguna de las tres no se cumple, el defecto permanece **latente**: está ahí, pero es invisible.

Aplicado literalmente a nuestro archivo:

- El defecto de la **línea 12** (`total / socios`, sin validar el divisor) puede vivir años intacto: si
  durante toda la historia operativa de la empresa **jamás** se registró un escenario con `socios = 0`
  —porque comercialmente no tiene sentido un fondo sin socios—, la línea se ejecuta miles de veces sin
  producir un solo `ZeroDivisionError`. El defecto no desapareció: nunca fue alcanzado por el dato que lo
  activa. Basta un día con un formulario vacío, una migración de datos o un usuario nuevo para que el
  fallo aparezca "de repente" en un código que "llevaba años funcionando".
- El defecto de la **línea 9** (`meses ** 2`) es todavía más silencioso: existe un valor de entrada,
  `meses = 1`, para el cual `1 ** 2 == 1` y el resultado coincide exactamente con el correcto. Si el
  negocio solo hubiera operado con inversiones a un mes, el defecto habría estado presente en cada
  ejecución **sin producir jamás un fallo observable**.

Esto conecta directamente con dos principios de ISTQB:

- **Principio 1 (las pruebas muestran la presencia de defectos, no su ausencia):** años de operación sin
  incidentes no son evidencia de código sin defectos; son evidencia de que las combinaciones de entrada
  usadas hasta hoy no alcanzaron los defectos existentes.
- **Principio 2 (las pruebas exhaustivas son imposibles):** el espacio de entradas de estas tres variables
  es prácticamente infinito, así que siempre quedarán rutas nunca ejercitadas donde un defecto puede
  esconderse indefinidamente.

**Conclusión:** la ausencia de fallos mide la suerte de la cobertura histórica de datos, no la calidad
interna del código. Por eso el testing sistemático de valores límite —precisamente `socios = 0`— es lo que
convierte un defecto latente en un fallo controlado dentro del laboratorio, en lugar de un incidente en
producción.

## Desafío Lógico 2

> Imaginen que corrigen todos los bugs y el script funciona perfecto, pero el cliente afirma que
> "necesitaba un sistema para calcular nóminas, no presupuestos". ¿Qué principio fundamental del testing
> de ISTQB se acaba de violar aunque el código esté limpio?

Se violó el **Principio 7 de ISTQB: la falacia de la ausencia de errores**
*(absence-of-errors fallacy)*.

Este principio establece que **encontrar y corregir defectos no sirve de nada si el sistema construido no
satisface las necesidades y expectativas reales del usuario**. Un software puede ser técnicamente
impecable —cero excepciones, cobertura completa, todos los casos en **Passed**— y aun así ser un **fracaso
absoluto de proyecto**, porque la calidad no se define contra el código, sino contra la necesidad que debía
resolver.

La distinción técnica que explica el desastre es **Verificación vs. Validación**:

| | Pregunta que responde | En este escenario |
|---|---|---|
| **Verificación** | ¿Estamos construyendo el producto **correctamente**? | ✅ Superada: fórmula de interés arreglada, división protegida, entradas validadas |
| **Validación** | ¿Estamos construyendo el **producto correcto**? | ❌ Fallida: el cliente pidió nóminas y recibió presupuestos |

Todo el esfuerzo se concentró en la **verificación** (calidad interna) y se omitió por completo la
**validación** (calidad externa, ajuste al propósito). El equipo probó exhaustivamente **el sistema
equivocado**.

**¿Dónde estuvo la causa raíz?** No en el testing dinámico, sino mucho antes: en un **Error** de
levantamiento y comprensión de requisitos. Ese Error se materializó como un **Defecto de requisitos** en el
documento base —no en una línea de Python—, y de ahí se propagó a una arquitectura entera perfectamente
construida sobre la premisa incorrecta. El **Fallo** solo se hizo visible en la entrega, que es el momento
más caro posible para descubrirlo.

Esto arrastra la violación de otros dos principios:

- **Principio 3 (pruebas tempranas / shift-left):** una revisión estática de los requisitos —una prueba de
  Caja Negra sobre el **documento**, no sobre el código— habría detectado la discrepancia en la primera
  semana, con un costo de corrección cercano a cero.
- **Principio 6 (las pruebas dependen del contexto):** un sistema de nóminas exige reglas de negocio
  radicalmente distintas (deducciones, aportes de seguridad social, retención en la fuente, periodicidad
  de pago) que jamás formaron parte del diseño de pruebas de un módulo de presupuestos.

**Lección de ingeniería:** la calidad no es la ausencia de errores técnicos, sino la **aptitud para el
uso** *(fitness for purpose)*. Un sistema con bugs que resuelve el problema correcto todavía puede
repararse; un sistema perfecto que resuelve el problema equivocado se tira a la basura.

---

## Check-list de Autoevaluación Final

- [x] Repositorio de GitHub estrictamente **público**
- [x] Contiene `presupuesto_analisis.py` **tal como fue entregado** (defectos intactos)
- [x] Contiene `casos_prueba.md`
- [x] El Markdown incluye evidencia del **mapa conceptual** (diagrama Mermaid renderizable al inicio del archivo)
- [x] La tabla tiene los casos **ejecutados**, con columna **Estado** y las **líneas de código defectuosas** señaladas (L3–L5, L9, L12)
- [x] `README.md` contiene las respuestas a los **dos desafíos** del cierre
- [x] Cada actividad fue observada y registrada de principio a fin
