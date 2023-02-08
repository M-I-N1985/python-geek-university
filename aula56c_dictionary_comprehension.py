"""
dictionary comprehension

sempre lembrar que se usarmos uma lista para iterarmos ou algo do tipo, para um dicionario, ele
não irá valorar para as chaves os itens repetidos da lista

"""
# misturando listas

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)