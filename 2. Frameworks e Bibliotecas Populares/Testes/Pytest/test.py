import pytest

def soma(a, b):
    return a + b

@pytest.fixture
def numeros_base():
    return (2, 3)

def test_soma_basica(numeros_base):
    a, b = numeros_base
    assert soma(a, b) == 5

@pytest.mark.parametrize(
    "a, b, resultado_esperado",
    [
        (1, 1, 2),
        (0, 0, 0),
        (2, 5, 7),
        (-1, 1, 0),
    ],
)

def test_soma_parametrizada(a, b, resultado_esperado):
    assert soma(a, b) == resultado_esperado