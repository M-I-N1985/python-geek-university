"""
try/except - para tratar erros, prevenindo que o programa pare de funcionar e o usuario receba msg inesperada

A forma mais simpes é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

"""

# Erro Generico - Não é a melhor forma especifica
try:
    len(5)
except:
    print('Houve algum problema')




# Erro Especifico