"""
Utilizando LC podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension

[ dado for dado in iteravel ]

# para entender o que está acontecendo devemos dividir a expressão em duas partes:
- a primeira parte: for numero in numeros
- a segunda parte: numero * 10

ex:
numeros: [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

"""
print('ex1:')
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

print('')
print('ex2:')

# obs: feito com loop for, o mais refatorado que fica seria assim:
numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# olha a diferença com LC, podemos fazer tudo em uma linha somente
print([numero * 2 for numero in [1, 2, 3, 4, 5]])