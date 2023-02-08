"""
Decorators com diferentes assinaturas

#  Relembrando

def gritar(funcao):
    def aumentar(param_funcao):
        return funcao(param_funcao).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu me chamo {nome}'

# Testando

print(saudacao('Taína'))

#  Passando uma função com dois param. para ser decorada com o mesmo decorador
#  Como resolver? R: Utilizando um padrao de proj. chamado Decorator Pattern

#  Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu me chamo {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


#  Testando 2

print(saudacao('Taína'))

print(ordenar('Picanha', 'Batata Frita'))


A assinatura de uma funcao é representada por seu retorno, nome e paramentro de entrada.
OBS: Vale lembrar que podemos utilizar parametros nomeados

"""

#  Decorators com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

print(soma_dez(1, 13))
print(comida_favorita('Maça', 'pizza'))