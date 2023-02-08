"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime

"""

import datetime


# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2023-01-23 10:46:15.629430   BR 23/01/2023

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes ma data/hora
inicio = datetime.datetime.now()
print(inicio)

# Altera o horário para 16 horas, 0 mintutos, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=11, minute=0, second=0, microsecond=0)

print(inicio)