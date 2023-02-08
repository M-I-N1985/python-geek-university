"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime

"""


import datetime


evento = datetime.datetime(2023, 1, 1, 0)
print(type(evento))
print(type('31/12/2023'))

print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yy): ")
nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
