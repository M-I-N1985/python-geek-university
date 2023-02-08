"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime

"""


import datetime


evento = datetime.datetime.now()

# Acessa individual dos elementos data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento))
