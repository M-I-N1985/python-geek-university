"""
**kwargs

poderiamos chamr este parametro de *xis, mas por convenção chamamos de **kwargs
Este é só mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parametros nomeados, e
tranforma esses parametros extras em um dicionário.



#  Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(iuri= 'verde', taina='rosa', huayra='amarelo', ana='azul')
cores_favoritas()
cores_favoritas(geek='navy')


#  Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek']=='Python':
        return f'Olá, você recebeu um comprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))



#  Nas nossa funções podemos ter (neta ordem):
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

"""
"""
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(24, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

"""
"""
def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {'nome': 'Felicity', 'sobrenome':'Jones'}
print(mostra_nomes(nome="Felicity", sobrenome="Jones"))

#  da maneira feito abaixo, não funciona
#  print(mostra_nomes(nomes))

# agora feito de maneira correta
print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

soma_multiplos_numeros(1, 2, 3)
"""

# ou então
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS: os nomes das chaves no dicionario devem ser os mesmos das funções
# dicionario2 = dict(a=1, b=2, c=3)  #  TypeError
# soma_multiplos_numeros(**dicionario2)

