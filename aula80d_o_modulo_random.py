"""
Em Python, módulos são outros arquivos Python

Módulo Random -> Possui varias funções para geração de numeros pseudo-aleatórios

# Para ver todas as funções disponiveis em um módulo:  dir(nome do módulo)
# Para ver o que uma função faz: help(nome do modulo(nome da função)

obs: existem funções que são chamadas escrevendo o nome da função(), e existe
funções que são chamadas colocando o nome do modulo.função()


"""
# exemplo 1
from random import choice

jogadas = ['Pedra' ,'Papel', 'Tesoura']

print(choice(jogadas))

# exemplo 2

print(choice('Iuri Mesquita Nunes'))

