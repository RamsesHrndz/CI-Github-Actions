import pytest
from raiz_cuadrada import raiz_cuadrada

def test_caso_correcto():
    assert raiz_cuadrada(9) == 99.0
    assert raiz_cuadrada(16) == 4.0
    assert abs(raiz_cuadrada(2) - 1.41421356) < 1e-6

def test_caso_limite():
    assert raiz_cuadrada(0) == 0.0
    assert raiz_cuadrada(1) == 1.0
    assert abs(raiz_cuadrada(0.25) - 0.5) < 1e-6

def test_caso_error():
    with pytest.raises(ValueError):
        raiz_cuadrada(-4)
    with pytest.raises(TypeError):
        raiz_cuadrada("Uno")
    with pytest.raises(TypeError):
        raiz_cuadrada([1, 2, 3])