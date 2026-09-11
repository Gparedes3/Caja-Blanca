"""Pruebas unitarias: un caso por cada tipo que pide la rúbrica."""

import pytest

from calculadora import calcular_cuota, calcular_intereses


def test_caso_feliz():
    # Datos normales: presupuesto x 0.02 x meses.
    assert calcular_intereses(100000, 6) == 12000


def test_valor_limite():
    # meses = 0 es el borde entre "sin inversión" y "un mes".
    assert calcular_intereses(100000, 0) == 0


def test_division_por_cero():
    # Antes: ZeroDivisionError sin control. Ahora: error claro.
    with pytest.raises(ValueError):
        calcular_cuota(50000, 0)


def test_input_negativo():
    # Un presupuesto negativo se rechaza, no se calcula.
    with pytest.raises(ValueError):
        calcular_intereses(-5000, 6)
