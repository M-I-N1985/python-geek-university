"""
dictionary comprehension

sempre lembrar que se usarmos uma lista para iterarmos ou algo do tipo, para um dicionario, ele
não irá valorar para as chaves os itens repetidos da lista

"""
# Gerando a partir de uma lista

numeros = [1, 2, 3, 4, 5]


quadrado = {str(valor): valor ** 2 for valor in numeros}
print(quadrado)