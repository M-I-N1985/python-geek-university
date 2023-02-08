"""
Generators (ocupa menos recurso em memória)

vimos LC, DC, SC e agora vamos ver generators(seria como tuple comprehension)

"""
# Qual a utilidade de um getsizeof()? -> Retorna a quantidade de bytes
# em memória do elemento passado como paramentro
# OBS: é necessário importar a biblioteca sys

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
# Gerando uma lista de números com Generator
gen = getsizeof((x * 10 for x in range(1000)))

print('Para fazermos as mesmas tarefas gastamos em momória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generators Expression: {gen} bytes')