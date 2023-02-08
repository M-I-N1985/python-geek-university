"""
#### O que melhor explica geradores e iteradores seria compará-los a uma lista.
uma lista é uma sequencia inteira, ou seja, se eu fizer uma lista de 10 numeros eu
terei 10 numeros gravado em algum lugar da memmória.
Agora, se eu fizer um iter, ou um generator, eu posso ter esses mesmos 10 numeros, mas
mas eles vão sendo criados a partir do momento que vão sendo chamados, com for, while,
next ou yield.

Generators são Iterators, mas o contrario não é verdadeiro.

Generators podem ser criados com funções geradoras
funçõ9es geradoreas utilizam a palavra reservadoa yield
generators podem ser criados com expreszseõs geradores

diferenças entre função e generators functionas (funções geradoras)

---------------------------------------------------------------------------
/Funções                        / Generator Functions                     /
---------------------------------------------------------------------------
/ Utilizam return               / Utilizam Yield                          /
---------------------------------------------------------------------------
/ retorna uma vez               / pode utilizar Yield multiplas vezes     /
---------------------------------------------------------------------------
/ quando executada, retorna algo / quando executada, retorna um generator /
---------------------------------------------------------------------------
"""

# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator

gen = conta_ate(4)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
