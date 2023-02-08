"""
Doctests

neste exemplo ele não reconhece as aspas duplas pois a docstrint contem aspas duplas 3 vezes

no terminal: python -m doctest -v aula143d_doctests.py

OBS: dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples
OBS2: não pode haver espaço ou tabs sem finalidades, pois pode ocorrer erros. Ourtras ferramentas como o
sublime test detectam estes erros, mas o pycharm releva

"""

def fala_oi():
    """Fala_oi()

    >>> fala_oi()
    'oi'
    """
    return "oi"


