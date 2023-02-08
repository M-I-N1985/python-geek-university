'''
Funções de Maior Grandeza - Higher Order Functions - HOF

O qye isso signigica?

- Quando uma liguagem de programação suporta HOF, indica que podemos ter funcoes
que retornam outras funções como resultado ou até mesmo passar funcoes como argumentos
para outras funções, e até mesmo criar variveis do tipo funções nos nosso programas.

OBS: Na seção de funções nós utilizamos isso.

Em Python as funções são Cidadões de primeira classe, First Class Citzen


# Nested Function - Funcoes Aninhadas

# Exemplo - definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


Em Python podemos tambem ter funcoes dentro de funcoes, que são conhecidas 
por Nested Functions ou tbm Inner Functions (Funções internas).

# Retornando a execucao da funcao
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você ')) # observe que a função sorteia aleatoriamente dentre de uma tupla

    return humor() + pessoa

print(cumprimento("Taina"))

# Retornando a funcao sem ser executada

def faz_me_rir():
    def rir():
        return choice(('hahahahahhaahah', 'kkkkkkkkkkkkkkk', 'yayayayayayayayayay'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())

'''

from random import choice


#  Inner Functions (Funções Internas / Nested Functions)
#  podem acessar o escopo de fuções mais externas

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'hihihi', 'huashashua'))
        return f'{risada} {pessoa}'
    return dando_risada
    #return dando_risada()
#print(faz_me_rir_novamente('Taina'))
# Testando

rindo = faz_me_rir_novamente('Taina')
print(rindo())
print(rindo())
print(rindo())
