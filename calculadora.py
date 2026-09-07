"""Versión corregida de la calculadora de presupuestos.

`presupuesto_analisis.py` se deja intacto, con sus defectos, porque es la
evidencia del taller. Aquí están las mismas operaciones ya arregladas y
partidas en funciones pequeñas, para poder probarlas una por una.
"""

TASA_MENSUAL = 0.02


def a_numero(texto, entero=False):
    """Convierte texto a número. Si no se puede, avisa con un mensaje claro.

    Arregla el defecto de las líneas 3-5: el original hacía float(input(...))
    sin protección y se caía con cualquier letra.
    """
    try:
        return int(texto) if entero else float(texto)
    except (TypeError, ValueError):
        raise ValueError(f"'{texto}' no es un número válido")


def calcular_intereses(presupuesto, meses):
    """Interés simple: presupuesto x tasa x meses.

    Arregla el defecto de la línea 9, que elevaba los meses al cuadrado.
    """
    if presupuesto < 0:
        raise ValueError("El presupuesto no puede ser negativo")
    if meses < 0:
        raise ValueError("Los meses no pueden ser negativos")
    return presupuesto * TASA_MENSUAL * meses


def calcular_cuota(total, socios):
    """Reparte el total entre los socios.

    Arregla el defecto de la línea 12, que dividía sin revisar el divisor.
    """
    if socios <= 0:
        raise ValueError("El número de socios debe ser mayor a 0")
    return total / socios


def analizar(presupuesto, socios, meses):
    """Junta todo y devuelve el resultado completo."""
    intereses = calcular_intereses(presupuesto, meses)
    total = presupuesto + intereses
    return {
        "presupuesto": presupuesto,
        "intereses": intereses,
        "total": total,
        "cuota_por_socio": calcular_cuota(total, socios),
    }


def pedir(mensaje, entero=False):
    """Pide un dato y vuelve a preguntar hasta que sea válido."""
    while True:
        try:
            return a_numero(input(mensaje), entero)
        except ValueError as error:
            print(error)


def main():
    print("=== Sistema de Análisis de Presupuesto ===\n")
    presupuesto = pedir("Ingrese el presupuesto total: ")
    socios = pedir("Ingrese el número de socios: ", entero=True)
    meses = pedir("Ingrese los meses de inversión: ", entero=True)

    try:
        r = analizar(presupuesto, socios, meses)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print(f"\nPresupuesto inicial: ${r['presupuesto']:.2f}")
    print(f"Intereses generados: ${r['intereses']:.2f}")
    print(f"Total con intereses: ${r['total']:.2f}")
    print(f"Cuota por socio ({socios} socios): ${r['cuota_por_socio']:.2f}")


if __name__ == "__main__":
    main()
