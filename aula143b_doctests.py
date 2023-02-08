"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.
Para rodar um test do doctest:
python -m doctest -v nome_do_modulo.py

se eu for tentar utilizar essa função com outras variaveis no pycharm
teremos problemas pois teremos aqueles doctests. mas no console funciona normalmente

Lembrando: se executarmos o teste fora do terminal (diretamente no pycharm) os 4 testes irão apresentar problemas

OBS: O pycharm roda com erro esse teste pois p o doctest com esses ">>>" é utilizado para rodar no console
"""

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]




