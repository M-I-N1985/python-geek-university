"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.
Para rodar um test do doctest:
python -m doctest -v nome_do_modulo.py

se eu for tentar utilizar essa função com outras variaveis no pycharm
teremos problemas pois teremos aqueles doctests. mas no console funciona normalmente


OBS: O pycharm roda com erro esse teste pois p o doctest com esses ">>>" é utilizado para rodar no console
"""

def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    100
    """
    return a + b

print(soma(3, 4))  # 7


