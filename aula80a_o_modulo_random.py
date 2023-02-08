"""
Em Python, módulos são outros arquivos Python

Módulo Random -> Possui varias funções para geração de numeros pseudo-aleatórios

# Para ver todas as funções disponiveis em um módulo:  dir(nome do módulo)
# Para ver o que uma função faz: help(nome do modulo(nome da função)

obs: existem funções que são chamadas escrevendo o nome da função(), e existe
funções que são chamadas colocando o nome do modulo.função()


"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (não recomendado)

import random

# OBS: ao realizar o import de todo o módlo, todas as funções, atributos, classes e propriedades que
# estiverem dentro do módulo ficarão disponiveis (ficarão na memória). Caso você saiba quais
# funções você precisa utilizar deste modulo, então não seria a forma ideal de utilização.

print(dir(random))
print(help(random.random))
print(random.random())
print("")

# Forma 2 - Importando uma função especifica do módulo

from random import random

for i in range(10):
    print(random())


