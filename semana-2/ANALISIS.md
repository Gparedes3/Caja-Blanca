# Análisis metacognitivo

Tres preguntas sobre lo que realmente significa este pipeline, más allá de que "corra".

## 1. ¿Por qué correr las pruebas en la nube (GitHub Actions) y no solo en local?

Correrlas en local ya nos decía si las 4 pruebas pasaban en *nuestra* máquina — pero eso
solo prueba que funciona con la versión de Python, las librerías y el estado del disco que
cada uno tiene en su laptop. Es el clásico "en mi máquina sí funciona".

La CI en la nube resuelve tres problemas que lo local no puede:

- **Reproducibilidad real.** Cada corrida arranca una máquina limpia (Ubuntu, sin nada
  instalado). Si el pipeline pasa ahí, pasa en cualquier lado — no depende de qué tenga
  instalado quien lo corrió.
- **No depende de que alguien se acuerde.** Si las pruebas solo viven en local, dependen de
  la disciplina de cada persona de correrlas antes de subir código. En la nube, `ci_pipeline.yml`
  se dispara solo en cada `push` y `pull request`: nadie puede "olvidarse".
- **Cobertura de versiones en paralelo.** Nuestra matriz corre Python 3.11 *y* 3.12 al mismo
  tiempo, en máquinas distintas. Probar eso en local significaría instalar y cambiar de
  versión manualmente cada vez.

En corto: local es para el ciclo rápido mientras escribimos código; la nube es la que
certifica, para todo el equipo, que ese código es seguro de mezclar con el de los demás.

## 2. ¿Qué significa realmente la luz verde?

Significa exactamente esto y nada más: **los 4 casos que pensamos escribir pasaron, en
las dos versiones de Python que probamos, en el momento en que corrió el pipeline.**

No significa que el software esté libre de errores. Esto es el Principio 1 de ISTQB en
la práctica: las pruebas muestran la presencia de defectos, no su ausencia. Nuestro propio
proyecto lo prueba — `calculadora.py` puede tener hoy un defecto que ninguno de los 4
tests toca (por ejemplo, nunca probamos un presupuesto tan grande que provoque overflow,
o meses no enteros). La luz verde es una foto acotada al conjunto de casos que se nos
ocurrió escribir, no un certificado de perfección.

Tratarla como "no hay bugs" es exactamente la falacia de la ausencia de errores (Principio 7):
la luz verde certifica que el código hace lo que *nosotros* le pedimos verificar, no que
haga lo que el negocio necesita ni que esté libre de todo defecto posible.

## 3. Exit Criteria bajo presión de entrega

El escenario real: es la noche antes de la entrega, hay un test en rojo (por ejemplo,
`test_cuota_con_cero_socios` falla porque alguien tocó `calcular_cuota` sin querer), y
la tentación es mergear igual porque "es solo un caso raro".

Nuestra postura: **el criterio de salida no se baja, se declara.** Bajar el estándar
(mergear con rojo, o borrar el test que molesta) no elimina el riesgo, solo lo esconde —
y lo mueve del lugar más barato para encontrarlo (ahora, en CI) al más caro (en producción,
con un socio real dividiendo entre cero). Eso choca directo con la idea de que cuanto antes
se detecta un defecto, más barato sale arreglarlo (Principio 3: probar temprano).

Lo que sí es válido bajo presión, según ISO 29119, es una **salida condicional
documentada**: si de verdad hay que entregar con ese caso sin resolver, se registra
explícitamente como riesgo aceptado (qué falla, por qué se acepta, quién lo aprobó) en vez
de simplemente ignorar el rojo. La diferencia entre "aceptar un riesgo conocido" y
"mergear con la CI en rojo sin decir nada" es toda la diferencia entre gestionar calidad
y solo aparentarla.
