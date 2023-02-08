
def gritar(funcao):
    def aumentar(param_funcao):
        return funcao(param_funcao).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu me chamo {nome}'

# Testando

print(saudacao('Taína'))