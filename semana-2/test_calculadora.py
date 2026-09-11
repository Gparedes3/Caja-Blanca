"""Unit tests de la versión corregida.

Cada test llama una función con datos y comprueba lo que devuelve.
Aquí todo pasa, porque el código ya está arreglado.
"""

import pytest

from calculadora import (
    a_numero,
    analizar,
    calcular_cuota,
    calcular_intereses,
)


# --- calcular_intereses -----------------------------------------------------

def test_intereses_con_datos_normales():
    assert calcular_intereses(100000, 6) == 12000


@pytest.mark.parametrize("presupuesto, meses, esperado", [
    (100000, 1, 2000),
    (100000, 6, 12000),
    (100000, 12, 24000),
    (50000, 3, 3000),
    (100000, 0, 0),
])
def test_intereses_con_varios_valores(presupuesto, meses, esperado):
    assert calcular_intereses(presupuesto, meses) == esperado


def test_intereses_rechaza_presupuesto_negativo():
    with pytest.raises(ValueError):
        calcular_intereses(-5000, 6)


def test_intereses_rechaza_meses_negativos():
    with pytest.raises(ValueError):
        calcular_intereses(100000, -6)


# --- calcular_cuota ---------------------------------------------------------

def test_cuota_reparte_entre_los_socios():
    assert calcular_cuota(112000, 4) == 28000


def test_cuota_con_un_solo_socio():
    assert calcular_cuota(112000, 1) == 112000


def test_cuota_con_cero_socios():
    with pytest.raises(ValueError):
        calcular_cuota(50000, 0)


def test_cuota_con_socios_negativos():
    with pytest.raises(ValueError):
        calcular_cuota(50000, -3)


# --- a_numero ---------------------------------------------------------------

def test_a_numero_convierte_decimales():
    assert a_numero("100000.50") == 100000.50


def test_a_numero_convierte_enteros():
    assert a_numero("4", entero=True) == 4


def test_a_numero_rechaza_texto():
    with pytest.raises(ValueError):
        a_numero("abc")


# --- analizar ---------------------------------------------------------------

def test_analizar_devuelve_todo_el_calculo():
    resultado = analizar(presupuesto=100000, socios=4, meses=6)

    assert resultado["intereses"] == 12000
    assert resultado["total"] == 112000
    assert resultado["cuota_por_socio"] == 28000
