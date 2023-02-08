"""
zip() Cria um iterável(zip object) que agrega elementos de cada um dos iteráveis com entrada em pares
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = ['a', 'b', 'c', 'd', 'e']

zip1 = zip(lista1, lista2, 'abc')  # para dicionário não funciona com o ultimo item

print(zip1)
print(type(zip1))

# Sempre podemos gerar iteráveis

print(list(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

print(set(zip1))
print('acontece o mesmo que em map(), filters() generators()')
print('some da memória após ser usado')

zip2 = zip(lista1, lista2)
print(dict(zip2))
zip3 = zip(lista3, lista2)
print(dict(zip3))
print('mesmo a lista 3 tendo 5 itens o zip se baseia no iterável de menor valor')

