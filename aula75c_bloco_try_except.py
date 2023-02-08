"""
try/except - para tratar erros, prevenindo que o programa pare de funcionar e o usuario receba msg inesperada

A forma mais simpes é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

"""

# Erro Especifico 4

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'A chave inserida não está contida neste dicionario'
    except TypeError:
        return 'O elemento precisa ser um dicionário'

dic = {'Chave': 'Valor'}
print(pega_valor(dic, 'Chave'))
print(pega_valor(dic, 'Casa'))
print(pega_valor(0, 'Chave'))



