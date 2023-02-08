"""
Any e all

all() => Retorna True se, todos os elementos do iteravel saõ verdadeiros ou ainda se o iterável
está vazio.

O iteravel pode ser uma tupla, um set, uma string

any() => Retorna True se, algum dos elementos de iterável for verdadeiro, se
o iteravel estiver vazio retorna False.

"""
print(all([0]))
print(any([0]))
print(all([0, 1, 2, 3, 4]))
print(any([0, 1, 2, 3, 4]))
print(all([0, 0, 0, 3, 0]))
print(any([0, 0, 0, 3, 0]))
print()

# mesmos exemplos que havia feito com all(), agora com any()
print(any([letra for letra in "aio" if letra in 'aeiou']))
print(any([letra for letra in "bcv" if letra in 'aeiou']))
