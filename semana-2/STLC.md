# Mapeo al STLC (ISTQB / ISO 29119)

Todo lo que hicimos en este taller —desde el mapa conceptual hasta la CI en verde— encaja
en las fases formales del **Software Testing Life Cycle**. Aquí está el mapeo, tarea por
tarea, y los criterios que decidimos usar para entrar y salir del ciclo.

## Fases

| Fase STLC | Qué hicimos nosotros |
|---|---|
| **1. Test Planning & Control** | Actividad 3: decidimos la estrategia (partición de equivalencia + valores límite) antes de tocar el código, y definimos el oráculo (`interés = presupuesto × 0.02 × meses`). También la decisión de automatizar con pytest y correrlo en CI en cada push. |
| **2. Test Analysis** | Leer qué *debía* hacer `presupuesto_analisis.py` a partir del enunciado (no del código) y derivar condiciones de prueba: presupuesto {negativo, cero, positivo, texto}, socios {≤0, ≥1}, meses {0, positivo}. |
| **3. Test Design** | Convertir esas condiciones en los casos concretos CP-01 a CP-04 (entrada exacta + resultado esperado), y más tarde en los `@pytest.mark.parametrize` de `test_calculadora.py`, que son el mismo diseño pero ejecutable. |
| **4. Test Environment Setup / Implementation** | Instalar `pytest`, escribir las 16 funciones `test_*`, y configurar `.github/workflows/ci_pipeline.yml` para que el entorno se levante solo (Ubuntu + Python 3.11/3.12) en cada corrida. |
| **5. Test Execution** | Actividad 4: correr los 4 casos a mano contra `presupuesto_analisis.py` (4 Failed). Después, correr `pytest -v` contra `calculadora.py` (16 Passed) y dejar que la CI lo repita en cada push. |
| **6. Test Completion (Closure)** | `casos_prueba.md` como reporte consolidado de defectos, el checklist final del README, y las lecciones (Desafíos 1 y 2) que quedan como cierre para la próxima vez que alguien toque este código. |

## Criterios de Entrada (Entry Criteria)

Condiciones que tuvieron que cumplirse **antes** de poder ejecutar la primera prueba real:

1. **El código bajo prueba existe y es estable.** `presupuesto_analisis.py` estaba entregado
   y congelado como evidencia; `calculadora.py` compila e importa sin errores de sintaxis.
   Sin esto no hay nada contra qué correr un `assert`.
2. **El oráculo está definido.** Antes de escribir un solo test tuvimos que acordar cuál es
   el resultado *correcto* (`presupuesto × 0.02 × meses`, `total / socios`). Un test sin
   oráculo no prueba nada, solo repite lo que el código ya hace.

## Criterios de Salida (Exit Criteria)

Condiciones que definimos para decir "esta ronda de pruebas terminó":

1. **Las 16 pruebas automatizadas pasan en verde**, tanto en local como en la matriz de CI
   (Python 3.11 y 3.12). Un pipeline en rojo sin resolver bloquea la salida, no se negocia.
2. **Cada uno de los 4 defectos originales tiene al menos un test que lo cubre** (L3–L5,
   L9, L12, y la validación de negativos que faltaba). Si alguno de esos defectos
   reapareciera, un test tendría que fallar — eso es lo que cierra el ciclo, no solo que
   "no haya errores visibles".

Ver también [`ANALISIS.md`](ANALISIS.md) para la reflexión sobre qué significa realmente
la luz verde y qué pasa con estos criterios bajo presión de entrega.
