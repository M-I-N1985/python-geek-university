"""
Não confundir reversed() com reverse()
reverse() pertence somente a listas
reverser() funciona com qualquer iterável

"""

# Podemos iterar sobre o reversed

lista = [1, 2, 3]

res = reversed(lista)
print(res)
print(type(res))

# List
print(list(reversed(lista)))

# Tuple
print(tuple(reversed(lista)))

# Set (não tem uma ordem)
print(set(reversed(lista)))


