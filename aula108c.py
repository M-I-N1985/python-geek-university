
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

