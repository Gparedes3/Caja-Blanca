# Taller Autónomo de Pruebas de Caja Negra — `presupuesto_analisis.py`

**Repositorio:** https://github.com/Gparedes3/Caja-Blanca
**Referencias:** ISTQB Foundation Level · ISO/IEC/IEEE 29119

---

## Actividad 1 — Mapa Conceptual

> Evidencia del mapa conceptual embebida como diagrama Mermaid (se renderiza directamente en GitHub).
> Los tres bloques no están sueltos: la cadena causal explica **qué** se busca, los principios explican
> **por qué** nunca se termina de buscar, y los roles explican **quién** responde en cada momento.

```mermaid
graph TD

    subgraph MUSICA["MÚSICA — del sonido a la experiencia"]
        R["RUIDO<br/>Sonidos sin intención musical"]
        B["BEAT<br/>Patrón rítmico que organiza el tiempo"]
        M["MELODÍA<br/>Secuencia de notas que puede reconocerse"]
        H["ARMONÍA<br/>Notas que suenan juntas y generan contexto"]
        C["CANCIÓN<br/>La combinación estructurada de ritmo,<br/>melodía, armonía y letra"]
        R -->|"se puede transformar en"| B
        B -->|"sirve de base para"| M
        M -->|"se enriquece con"| H
        H -->|"junto con estructura y voz forma"| C
    end

    subgraph VIDEOJUEGOS["VIDEOJUEGOS — del jugador al mundo"]
        I["INPUT<br/>El jugador hace una acción"]
        G["GAME LOGIC<br/>El juego interpreta la acción"]
        S["STATE<br/>El mundo cambia de estado"]
        F["FEEDBACK<br/>El juego comunica lo ocurrido"]
        E["EXPERIENCIA<br/>El jugador interpreta y decide qué hacer"]
        I -->|"activa"| G
        G -->|"modifica"| S
        S -->|"produce"| F
        F -->|"genera"| E
        E -->|"provoca un nuevo"| I
    end

    subgraph COCINA["COCINA — de ingredientes a plato"]
        ING["INGREDIENTES<br/>Materia prima"]
        PRE["PREPARACIÓN<br/>Cortar, mezclar, sazonar"]
        CAL["COCCIÓN<br/>Transformación mediante calor"]
        PLA["PLATO<br/>Resultado físico"]
        SAB["EXPERIENCIA<br/>Aroma, textura, sabor y presentación"]
        ING -->|"se transforman mediante"| PRE
        PRE -->|"pasa por"| CAL
        CAL -->|"produce"| PLA
        PLA -->|"se convierte en"| SAB
    end

    subgraph ESPACIO["ESPACIO — de materia a universo"]
        POL["POLVO Y GAS<br/>Materia dispersa"]
        EST["ESTRELLA<br/>La gravedad concentra materia"]
        PLA2["PLANETA<br/>Materia orbitando una estrella"]
        SIS["SISTEMA<br/>Planetas, lunas, asteroides y otros cuerpos"]
        UNI["UNIVERSO<br/>Escala donde existen innumerables sistemas"]
        POL -->|"la gravedad puede formar"| EST
        EST -->|"puede estar acompañada por"| PLA2
        PLA2 -->|"forma parte de un"| SIS
        SIS -->|"existe dentro del"| UNI
    end

    subgraph REDES["INTERNET — de una idea a una tendencia"]
        IDEA["IDEA<br/>Algo que alguien publica"]
        POST["POST<br/>Se convierte en contenido visible"]
        SHARE["COMPARTIR<br/>Otras personas lo redistribuyen"]
        TREND["TENDENCIA<br/>La idea alcanza mucha atención"]
        MEME["MEME<br/>La comunidad transforma y replica la idea"]
        IDEA -->|"se publica como"| POST
        POST -->|"puede generar"| SHARE
        SHARE -->|"acumula suficiente atención y crea una"| TREND
        TREND -->|"la comunidad puede convertirlo en"| MEME
        MEME -->|"genera nuevas"| IDEA
    end

    subgraph FOTOGRAFIA["FOTOGRAFÍA — de luz a imagen"]
        LUZ["LUZ<br/>Información física de la escena"]
        LENTE["LENTE<br/>Enfoca y dirige la luz"]
        SENSOR["SENSOR<br/>Convierte la luz en datos"]
        RAW["RAW<br/>Datos de imagen sin procesar"]
        FOTO["FOTOGRAFÍA<br/>Imagen procesada y visualizada"]
        LUZ -->|"entra por"| LENTE
        LENTE -->|"proyecta luz sobre"| SENSOR
        SENSOR -->|"registra"| RAW
        RAW -->|"se procesa para crear"| FOTO
    end

    subgraph TIEMPO["TIEMPO — de instante a recuerdo"]
        INST["INSTANTE<br/>Un momento que ocurre"]
        MOM["MOMENTO<br/>Una experiencia percibida"]
        REC["RECUERDO<br/>Información conservada por la mente"]
        HIST["HISTORIA<br/>Recuerdos organizados y contados"]
        MIT["MITO<br/>Una historia que puede transformarse<br/>con cada generación"]
        INST -->|"es vivido como"| MOM
        MOM -->|"puede convertirse en"| REC
        REC -->|"puede formar parte de una"| HIST
        HIST -->|"con el tiempo puede convertirse en"| MIT
    end

    %% --- CONEXIONES ENTRE TEMAS ---

    C -.->|"una canción puede convertirse en"| MEME
    MEME -.->|"puede inspirar una nueva"| FOTO
    FOTO -.->|"captura un"| MOM
    MOM -.->|"puede acompañarse de"| C
    PLA -.->|"puede aparecer en una"| FOTO
    FOTO -.->|"puede documentar una"| HIST
    VIDEOJUEGOS["VIDEOJUEGOS"] -.->|"también construyen"| HIST
    TREND -.->|"puede convertirse en referencia dentro de"| VIDEOJUEGOS
    UNI -.->|"contiene escenarios imaginados en"| VIDEOJUEGOS

    style R fill:#eeeeee,stroke:#616161,color:#000
    style B fill:#ffcc80,stroke:#ef6c00,color:#000
    style M fill:#ce93d8,stroke:#6a1b9a,color:#000
    style H fill:#90caf9,stroke:#1565c0,color:#000
    style C fill:#f48fb1,stroke:#ad1457,color:#000

    style I fill:#c5cae9,stroke:#283593,color:#000
    style G fill:#b39ddb,stroke:#4527a0,color:#000
    style S fill:#80cbc4,stroke:#00695c,color:#000
    style F fill:#81d4fa,stroke:#0277bd,color:#000
    style E fill:#a5d6a7,stroke:#2e7d32,color:#000

    style ING fill:#ffe0b2,stroke:#e65100,color:#000
    style PRE fill:#ffccbc,stroke:#d84315,color:#000
    style CAL fill:#ef9a9a,stroke:#c62828,color:#000
    style PLA fill:#fff59d,stroke:#f9a825,color:#000
    style SAB fill:#c8e6c9,stroke:#2e7d32,color:#000

    style POL fill:#b0bec5,stroke:#37474f,color:#000
    style EST fill:#ffab91,stroke:#d84315,color:#000
    style PLA2 fill:#90caf9,stroke:#1565c0,color:#000
    style SIS fill:#b39ddb,stroke:#512da8,color:#000
    style UNI fill:#263238,stroke:#000,color:#fff

    style IDEA fill:#fff9c4,stroke:#f9a825,color:#000
    style POST fill:#bbdefb,stroke:#1976d2,color:#000
    style SHARE fill:#c8e6c9,stroke:#388e3c,color:#000
    style TREND fill:#f8bbd0,stroke:#c2185b,color:#000
    style MEME fill:#d1c4e9,stroke:#512da8,color:#000

    style LUZ fill:#fff59d,stroke:#f9a825,color:#000
    style LENTE fill:#b0bec5,stroke:#455a64,color:#000
    style SENSOR fill:#90caf9,stroke:#1565c0,color:#000
    style RAW fill:#ce93d8,stroke:#6a1b9a,color:#000
    style FOTO fill:#80cbc4,stroke:#00695c,color:#000

    style INST fill:#e1bee7,stroke:#7b1fa2,color:#000
    style MOM fill:#f8bbd0,stroke:#c2185b,color:#000
    style REC fill:#bbdefb,stroke:#1565c0,color:#000
    style HIST fill:#c8e6c9,stroke:#2e7d32,color:#000
    style MIT fill:#ffcc80,stroke:#ef6c00,color:#000


### Idea que amarra los tres bloques

> **QA** intenta que el **Error** nunca ocurra (proceso), **QC** intenta que el **Defecto** no salga del taller
> (producto) y el **Testing** es la técnica que fuerza al **Fallo** a mostrarse en un ambiente controlado
> antes de que lo haga en producción. Los **7 principios** son las restricciones físicas del juego: nos dicen
> que nunca terminaremos (P1, P2), dónde y cuándo conviene buscar (P3, P4, P6), por qué debemos cambiar de
> táctica (P5), y que ganar técnicamente no es ganar si el producto no era el pedido (P7).

---

## Actividad 2 — Recepción y Verificación del Código Base

- Archivo `presupuesto_analisis.py` recibido **tal como fue entregado** (sin correcciones).
- Verificación de ejecución con datos normales (`presupuesto=100000`, `socios=4`, `meses=6`):
  el script arranca, pide las tres entradas e imprime el reporte completo **sin excepciones**.

```
=== Sistema de Análisis de Presupuesto ===
Presupuesto inicial: $100000.00
Intereses generados: $72000.00
Total con intereses: $172000.00
Cuota por socio (4 socios): $43000.00
```

> El programa **corre**, pero correr no es funcionar: el veredicto sobre ese `$72000.00` se emite en la
> Actividad 4, no aquí. (Principio 1)

---

## Actividad 3 — Diseño del Plan de Pruebas (Caja Negra Estática)

Diseño realizado **sin inspeccionar la estructura interna** del código, aplicando:

| Técnica | Aplicación en este sistema |
|---|---|
| **Partición de equivalencia** | `presupuesto`: {negativo} · {cero} · {positivo} · {no numérico} — `socios`: {≤0} · {≥1} · {no entero} — `meses`: {0} · {1..n} |
| **Valores límite** | `socios = 0` (frontera inferior inválida) y `socios = 1` (primer valor válido); `meses = 1` vs `meses = 12` |
| **Oráculo de negocio** | Interés simple mensual esperado: `presupuesto × 0.02 × meses`. Cuota esperada: `total ÷ socios`. |

### Tabla de casos — estado inicial: **planeado**

| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
|---|---|---|---|---|---|---|
| CP-01 | Cálculo de interés con datos normales (partición válida) | Script iniciado | presupuesto=100000, socios=4, meses=6 | Intereses = $12000.00 (100000 × 0.02 × 6), total = $112000.00, cuota = $28000.00 | — | — |
| CP-02 | Comportamiento en el límite inferior inválido de socios | Script iniciado, presupuesto > 0 | presupuesto=50000, socios=0, meses=3 | Mensaje controlado de error ("el número de socios debe ser mayor a 0"), sin cerrar el programa | — | — |
| CP-03 | Entrada no numérica en presupuesto (partición inválida) | Script iniciado | presupuesto="abc", socios=2, meses=3 | Mensaje controlado ("ingrese un valor numérico") y nueva solicitud del dato | — | — |
| CP-04 | Valores negativos en presupuesto y socios (partición inválida) | Script iniciado | presupuesto=-5000, socios=-3, meses=6 | Rechazo de valores negativos con mensaje controlado; no debe calcularse cuota alguna | — | — |

---

## Actividad 4 — Ejecución Dinámica y Localización de Defectos

Ejecución real del plan y, **solo después del fallo**, inspección de Caja Blanca para aislar el defecto físico.

### Tabla de casos — ejecutada

| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
|---|---|---|---|---|---|---|
| CP-01 | Cálculo de interés con datos normales | Script iniciado | presupuesto=100000, socios=4, meses=6 | Intereses = $12000.00, total = $112000.00, cuota = $28000.00 | Intereses = **$72000.00**, total = $172000.00, cuota = $43000.00. El programa **no se cae**: entrega un número creíble pero incorrecto (6× el valor real) | **Failed** |
| CP-02 | Límite inferior inválido de socios | Script iniciado, presupuesto > 0 | presupuesto=50000, socios=0, meses=3 | Mensaje controlado de error, sin cerrar el programa | `ZeroDivisionError: float division by zero` en línea 12 — el programa se detiene abruptamente | **Failed** |
| CP-03 | Entrada no numérica en presupuesto | Script iniciado | presupuesto="abc", socios=2, meses=3 | Mensaje controlado y nueva solicitud del dato | `ValueError: could not convert string to float: 'abc'` en línea 3 — el programa se detiene antes de pedir los otros datos | **Failed** |
| CP-04 | Valores negativos en presupuesto y socios | Script iniciado | presupuesto=-5000, socios=-3, meses=6 | Rechazo con mensaje controlado; sin cálculo de cuota | Acepta los negativos y calcula: intereses = $-3600.00, total = $-8600.00, **cuota = $2866.67 positiva** para una deuda negativa | **Failed** |

**Resumen:** 4 ejecutados · 0 Passed · **4 Failed**.

### Reportes de Defecto (Fallo ≠ Defecto)

**Reporte de Defecto: CP-01 → Defecto lógico de fórmula**
El **Fallo** (intereses inflados a $72000.00 en lugar de $12000.00) ocurre porque el **Defecto** está en la
**línea 9**:

```python
intereses = presupuesto * tasa_interes_mensual * (meses ** 2)
```

El requisito describe un interés **simple mensual**, que se acumula multiplicando por el número de meses;
el código eleva `meses` al cuadrado (`meses ** 2` = 36 en vez de 6). Es el defecto más peligroso del lote:
**no lanza excepción**, así que un usuario sin oráculo de negocio lo daría por "Passed". Corrección:
`* meses`.

**Reporte de Defecto: CP-02 → División sin validar el divisor**
El **Fallo** (`ZeroDivisionError`, el programa se detiene) ocurre porque el **Defecto** está en la
**línea 12**:

```python
cuota_por_socio = total / socios
```

El código nunca valida si `socios` es igual a cero antes de dividir. Falta la guarda previa
(`if socios <= 0:` con mensaje controlado) o el bloque `try/except ZeroDivisionError`.

**Reporte de Defecto: CP-03 → Conversión de tipo sin protección**
El **Fallo** (`ValueError`, caída al primer dato mal escrito) ocurre porque el **Defecto** está en la
**línea 3** — y se repite igual en las **líneas 4 y 5**:

```python
presupuesto = float(input("Ingrese el presupuesto total: "))
socios = int(input("Ingrese el número de socios: "))
meses  = int(input("Ingrese los meses de inversión: "))
```

Las conversiones `float()` / `int()` se aplican directamente sobre `input()` sin `try/except ValueError` ni
bucle de reintento. Un error de digitación derriba la aplicación completa.

**Reporte de Defecto: CP-04 → Ausencia de validación de dominio**
El **Fallo** (una deuda de $-8600.00 repartida como una cuota **positiva** de $2866.67) ocurre porque el
**Defecto** es una **omisión entre las líneas 5 y 9**: no existe ninguna validación de rango que rechace
`presupuesto < 0` ni `socios < 1`. Al dividir dos negativos, el signo se cancela y el sistema emite un
resultado matemáticamente válido pero **financieramente absurdo**. Corrección: validar el dominio de cada
entrada inmediatamente después de leerla.

### Trazabilidad defecto → principio ISTQB

| Caso | Fallo observado | Defecto (línea) | Principio que ilustra |
|---|---|---|---|
| CP-01 | Resultado incorrecto sin excepción | L9 — `meses ** 2` | P1: el sistema "funcionaba"; probar reveló el bug |
| CP-02 | `ZeroDivisionError` | L12 — división sin guarda | P2/P4: los defectos se agrupan en las fronteras |
| CP-03 | `ValueError` | L3 (y L4, L5) — casting sin `try` | P4: mismo patrón defectuoso repetido en un barrio de 3 líneas |
| CP-04 | Cuota positiva sobre monto negativo | L5–L9 — omisión de validación | P7: cálculo "correcto", requisito de negocio incumplido |

---

## Actividad 5 — Control de Versiones y Entrega

Artefactos versionados en el repositorio público:
`presupuesto_analisis.py` (íntegro, sin corregir) · `casos_prueba.md` · `README.md` · `.gitignore`
