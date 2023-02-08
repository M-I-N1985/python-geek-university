"""
Em Python, módulos são outros arquivos Python

Módulo Random -> Possui varias funções para geração de numeros pseudo-aleatórios

# Para ver todas as funções disponiveis em um módulo:  dir(nome do módulo)
# Para ver o que uma função faz: help(nome do modulo(nome da função)

obs: existem funções que são chamadas escrevendo o nome da função(), e existe
funções que são chamadas colocando o nome do modulo.função()


"""


# Forma 2 - Importando uma função especifica do módulo

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # o 7 não é incluido




