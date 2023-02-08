"""
dictionary comprehension

sempre lembrar que se usarmos uma lista para iterarmos ou algo do tipo, para um dicionario, ele
não irá valorar para as chaves os itens repetidos da lista

"""
# aplicando logica condicional em um dictionary comprehension

numeros = [1, 2, 3, 4, 5]

resultado = {str(numero): 'Par' if numero % 2 == 0 else 'impar' for numero in numeros}
print(resultado)