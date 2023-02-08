"""
Map

com map, fazemos mapeamento de valores para função.

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo o iterável.
# retorna um object


"""

import math

def area(r):
    """Calcula a area de um círculo com raio'r'."""
    return math.pi * (r ** 2)

print(area(2))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []
for i in raios:
    areas.append(area(i))
print(areas)

# Forma 2 com list comprehension

print([area(r) for r in raios])

# Forma 3 com maps

areas = map(area, raios)

print(areas)
print(type(areas))

# Tem que imprimir com lista

print(list(areas))

# Forma 4 com maps e lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar map pela primeira vez ele zera a função, ou seja, ele limpa a memória
# automáticamente

