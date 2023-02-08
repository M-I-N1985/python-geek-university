"""
Em Python, módulos são outros arquivos Python

Módulo Random -> Possui varias funções para geração de numeros pseudo-aleatórios

# Para ver todas as funções disponiveis em um módulo:  dir(nome do módulo)
# Para ver o que uma função faz: help(nome do modulo(nome da função)

obs: existem funções que são chamadas escrevendo o nome da função(), e existe
funções que são chamadas colocando o nome do modulo.função()


"""

from random import shuffle

# shuffle() -> tem a função de embaralhar dados

cartas = ['A', 'K', 'Q', 'J','10', '9', '8', '7', '6', '5', '4', '3', '2']

shuffle(cartas)

print(cartas)
print(cartas.pop())  # retira o ultimo valor da lista e retorna ele