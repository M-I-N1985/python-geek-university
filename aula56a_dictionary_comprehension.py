"""
dictionary comprehension

sempre lembrar que se usarmos uma lista para iterarmos ou algo do tipo, para um dicionario, ele
não irá valorar para as chaves os itens repetidos da lista

"""
# Gerando a partir de um dicionario
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(numeros.items())
print('')

quadrado = { chave: valor * 2 for chave, valor in numeros.items()}
print(quadrado)