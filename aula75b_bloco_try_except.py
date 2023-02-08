"""
try/except - para tratar erros, prevenindo que o programa pare de funcionar e o usuario receba msg inesperada

A forma mais simpes é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

"""

# Erro Especifico 1

try:
    geek()
except NameError:
    print('Você está informando uma função inexistente')

# Erro Especifico 2

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
