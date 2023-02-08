"""
Any e all

all() => Retorna True se todos os elementos do iteravel saõ verdadeiros ou ainda se o iterável
está vazio.

O iteravel pode ser uma tupla, um set, uma string

any() => Retorna True se, algum dos elementos de iterável for verdadeiro, se
o iteravel estiver vazio retorna False.

"""

# Exemplo all()
print(all([0]))
print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))
print(all(['']))
print(all([])) # iterável vazio
print()


nomes = ['Taína', 'Tassiana', 'Tito']
print(all([nome[0] == 'T' for nome in nomes])) # Ele avalia se todos os itens da lista iniciam com T
print()

# Esse na verdade foi um erro do professor, que tentou escrever algo que em algum momento não
# retornasse alguma letra, e que pudesse dar False quando aplicado all()
# mas no final virou uma tautologia, pois na LC se não tiver alguma letra volta um conjunto vazio
# ou seja, ou retorna uma letra, ou retorna um conjunto vazio, e sabemos que ambos são
# True para all()
# OBS: ele deveria ter feito algo com alguma condicional que retornasse uma string vazia, ou zero
print(all([letra for letra in "aio" if letra in 'aeiou']))
print([letra for letra in "aio" if letra in 'aeiou'])
print()
print(all([letra for letra in "bcv" if letra in 'aeiou']))
print([letra for letra in "bcv" if letra in 'aeiou'])
