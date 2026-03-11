from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]


def _load_module(relative_path: str, module_name: str):
    module_path = BASE_DIR / relative_path
    spec = spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Nao foi possivel carregar o modulo: {module_path}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_utils_dobro_retorna_valor_esperado():
    utils = _load_module(
        "1. Conhecimentos Técnicos Essenciais/recursos/exemplo_pacotes/utils.py",
        "utils_mod",
    )

    assert utils.dobro(4) == 8
    assert utils.dobro(-3) == -6


def test_utils_pi_tem_precision_basica():
    utils = _load_module(
        "1. Conhecimentos Técnicos Essenciais/recursos/exemplo_pacotes/utils.py",
        "utils_mod_pi",
    )

    assert round(utils.PI, 2) == 3.14


def test_funcoes_internas_quadrado_e_inverte_string():
    funcoes_internas = _load_module(
        "1. Conhecimentos Técnicos Essenciais/recursos/funcoes_internas.py",
        "funcoes_internas_mod",
    )

    assert funcoes_internas.quadrado(5) == 25
    assert funcoes_internas.inverte_string("Python") == "nohtyP"


def test_funcoes_internas_strings_pequenas():
    funcoes_internas = _load_module(
        "1. Conhecimentos Técnicos Essenciais/recursos/funcoes_internas.py",
        "funcoes_internas_mod_filter",
    )

    assert funcoes_internas.strings_pequenas("Ana") is True
    assert funcoes_internas.strings_pequenas("Carlos") is False
