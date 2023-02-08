"""
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

gen = conta_ate(10)

print(gen)

for num in gen:
    print(num)
