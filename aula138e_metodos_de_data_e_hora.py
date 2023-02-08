"""
Métodos de Data e Hora

# Formatando dat/horas com srtftime() (String Format Time)
# dd/mm/yyyy hora:minuto

http://docs.python.org/3/library/datetime.html

strftime() and strptime() behavior



"""

import datetime


hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d de %B de %Y')

print(hoje_formatado)
