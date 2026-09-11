# Semana 2 — De Caja Negra a Caja Blanca + CI/CD

Probamos un sistema de presupuesto que venía con defectos escondidos a propósito, lo
arreglamos, lo cubrimos con pruebas automatizadas y montamos un pipeline de CI/CD que
las corre solo en cada push.

**Equipo:**

| Rol | Integrante | De qué se encarga |
|---|---|---|
| Git Lead | Guillermo Paredes | Estructura del repo, merges, pipeline de CI/CD (`ci_pipeline.yml`) |
| Dev | Mateo Villacreses | Refactor de `presupuesto_analisis.py` → `calculadora.py`, arreglo de los 4 defectos |
| Tester | Donato Oña | Plan de pruebas (`casos_prueba.md`), diseño de casos y `test_calculadora.py` |

> Roles asignados según el historial de commits — ajústenlos si no reflejan quién hizo qué.

## Qué hay en esta carpeta

| Archivo | Qué es |
|---|---|
| `presupuesto_analisis.py` | El código que nos entregaron, **sin corregir** (la evidencia) |
| `calculadora.py` | La versión corregida, partida en funciones que se pueden probar |
| `casos_prueba.md` | Mapa conceptual, plan de pruebas, ejecución y los defectos encontrados |
| `STLC.md` | Mapeo de este taller a las fases del STLC (ISTQB/ISO 29119) y los criterios de entrada/salida |
| `ANALISIS.md` | Respuestas a las 3 preguntas de cierre: nube vs. local, qué significa la luz verde, exit criteria bajo presión |
| `image.png` | El mapa conceptual de la Actividad 1 |
| `README.md` | Este archivo, con las respuestas del cierre |
| `test_calculadora.py` | Las pruebas automáticas |
| `../.github/workflows/ci_pipeline.yml` | Pipeline de CI que corre las pruebas en cada push (Python 3.11 y 3.12) |

## Cómo ejecutarlo

```bash
python3 presupuesto_analisis.py
```

Pide tres datos por consola: presupuesto total, número de socios y meses de inversión.

## Resumen

Diseñamos 4 casos con partición de equivalencia y valores límite. Los cuatro fallaron.
Encontramos 4 defectos: en las líneas **3–5**, **9** y **12**, más una validación que
simplemente no existe. El detalle está en [`casos_prueba.md`](casos_prueba.md).

## Cómo ejecutar la versión corregida

```bash
python3 calculadora.py
```

## Pruebas automatizadas

Para correrlas en tu máquina:

```bash
pip install pytest
pytest
```

Son 4 pruebas en `test_calculadora.py`, una por cada tipo de caso: feliz, límite,
división por cero e input negativo. Cada una llama a una función con unos datos y
comprueba que devuelve lo que debe:

```python
def test_caso_feliz():
    assert calcular_intereses(100000, 6) == 12000
```

GitHub Actions las corre solo cada vez que subimos algo, gracias a
[`../.github/workflows/ci_pipeline.yml`](../.github/workflows/ci_pipeline.yml). Ver el
mapeo completo al STLC en [`STLC.md`](STLC.md) y la reflexión sobre qué significa la luz
verde de esa CI en [`ANALISIS.md`](ANALISIS.md).

---

# Cierre — Los dos desafíos

## Desafío 1

> ¿Puede un defecto vivir años en el código sin causar nunca un fallo?

**Sí, y nuestro propio código lo demuestra.**

El defecto es una línea mal escrita: está ahí desde que alguien la escribió. El fallo es algo que pasa,
en el momento en que ejecutas el programa. Para que un defecto se convierta en fallo tienen que darse
tres cosas a la vez:

1. Que la línea mala **se ejecute**.
2. Que se ejecute **con el dato** que activa el problema.
3. Que el resultado equivocado **se vea** en la salida.

Si falta cualquiera de las tres, el defecto sigue ahí pero nadie lo nota.

Dos ejemplos de nuestro archivo:

- **Línea 12** (`total / socios`, sin revisar el divisor): si en toda la vida de la empresa nunca nadie
  registró un fondo con cero socios —porque no tiene sentido comercial—, esa línea corre miles de veces
  sin un solo error. El defecto nunca se fue: solo nunca le llegó el dato que lo despierta. Un formulario
  vacío o una migración de datos, y un día aparece el fallo en un código que "llevaba años funcionando".
- **Línea 9** (`meses ** 2`): esta es todavía más silenciosa. Con `meses = 1`, `1 ** 2` da 1 y el
  resultado sale exactamente igual al correcto. Si la empresa solo hubiera trabajado con inversiones a
  un mes, el defecto habría estado presente siempre sin dar nunca un resultado malo.

Esto es justo lo que dicen dos principios de ISTQB:

- **P1 — las pruebas muestran que hay defectos, no que no los hay.** Años sin incidentes no significan
  código limpio; significan que los datos usados hasta hoy no tocaron los defectos que ya estaban.
- **P2 — probar todo es imposible.** Con tres variables numéricas las combinaciones son infinitas, así
  que siempre van a quedar caminos sin recorrer donde un defecto se puede esconder.

**En corto:** que no haya fallos mide la suerte de los datos que han entrado, no la calidad del código.
Por eso probamos valores límite como `socios = 0`: para que el defecto salga aquí y no en producción.

## Desafío 2

> Arreglan todos los bugs, el script queda perfecto, y el cliente dice: "yo necesitaba calcular nóminas,
> no presupuestos". ¿Qué principio se violó, aunque el código esté limpio?

**El Principio 7: la falacia de la ausencia de errores.**

Dice que encontrar y arreglar defectos no sirve de nada si el sistema no es lo que el usuario necesitaba.
Un programa puede estar impecable —cero excepciones, todos los casos en Passed— y aun así ser un fracaso,
porque la calidad no se mide contra el código sino contra el problema que debía resolver.

La diferencia que lo explica es **verificación vs. validación**:

| | Pregunta | En este caso |
|---|---|---|
| **Verificación** | ¿Lo estamos construyendo bien? | ✅ Sí: fórmula arreglada, división protegida, entradas validadas |
| **Validación** | ¿Estamos construyendo lo correcto? | ❌ No: pidieron nóminas y recibieron presupuestos |

Todo el esfuerzo se fue en verificar y nadie validó. Probamos muy bien el sistema equivocado.

**¿Dónde empezó todo?** No en las pruebas, mucho antes: en un **error** al entender los requisitos. Ese
error quedó como un defecto en el documento —no en una línea de Python— y de ahí se propagó a todo lo
demás. El fallo recién se vio en la entrega, que es el momento más caro para descubrirlo.

Y de paso se rompieron otros dos principios:

- **P3 — probar temprano:** revisar el documento de requisitos en la primera semana habría encontrado la
  confusión cuando corregirla no costaba casi nada.
- **P6 — las pruebas dependen del contexto:** un sistema de nóminas necesita reglas completamente
  distintas (deducciones, seguridad social, retenciones, periodicidad de pago) que nunca estuvieron en
  el diseño de pruebas de un módulo de presupuestos.

**La lección:** calidad no es que no haya errores, es que sirva para lo que se pidió. Un sistema con bugs
que resuelve el problema correcto todavía se arregla; uno perfecto que resuelve el problema equivocado
se bota.

---

## Check-list final

- [x] Repositorio de GitHub **público**
- [x] Incluye `presupuesto_analisis.py` tal como lo entregaron, sin corregir
- [x] Incluye `casos_prueba.md`
- [x] El Markdown muestra el **mapa conceptual** al inicio
- [x] La tabla tiene los casos **ejecutados**, con columna **Estado** y las **líneas defectuosas** (L3–L5, L9, L12)
- [x] El `README.md` responde los **dos desafíos** del cierre
- [x] Cada actividad quedó registrada de principio a fin
- [x] Las pruebas están automatizadas con **pytest** (`test_calculadora.py`), cubriendo caso
  feliz, valores límite, división por cero e inputs negativos
- [x] La **CI de GitHub Actions** las corre en cada push (`../.github/workflows/ci_pipeline.yml`)
  en Python 3.11 y 3.12
- [x] Mapeo a las fases del **STLC** con 2 criterios de entrada y 2 de salida (`STLC.md`)
- [x] Análisis metacognitivo de las 3 preguntas de cierre (`ANALISIS.md`)
- [x] Repositorio organizado en `/semana-2/`
