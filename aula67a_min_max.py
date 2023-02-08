"""
max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos
"""

# Exemplo

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

dicionario = {"a": 1, "b": 8, "c": 4, "d": 99, "e": 34, "f": 129}
print(max(dicionario))  # dessa frma ele informa quem é a maior chave
print(max(dicionario.values()))

conj1 = [ 'a', 'ab', 'abc']
print(max(conj1))

conj2 = ['a', 'b', 'c']
print(max(conj2))
print(max(['a', 'b', 'c']))

print(max("Iuri Mesquita Nunes"))


