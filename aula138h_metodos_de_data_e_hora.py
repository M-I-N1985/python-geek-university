"""
Métodos de Data e Hora

para funcionamento das funções abaixo é necessário instalar:

"""

import datetime

nascimento = datetime.datetime.strptime('10/06/1988', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual a sua data de nascimento? (dd/mm/yyyy) ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora

almoco = datetime.time(12, 30, 0)
print(almoco)
