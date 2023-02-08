"""
Métodos de Data e Hora

para funcionamento das funções abaixo é necessário instalar:

"""

import timeit
import functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
        return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))