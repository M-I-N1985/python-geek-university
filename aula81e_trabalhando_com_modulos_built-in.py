"""
Outra maneira de importar varios modulos

"""

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(4, 7))

lista = ['Iuri', 'Taína', 'Humberto', 'Neide']
shuffle(lista)

print(lista)

print(choice('Humberto'))