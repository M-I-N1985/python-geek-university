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

hoje_formatado = hoje.strftime('%d/%m/%Y')  # ano maíusculo
hoje_formatado2 = hoje.strftime('%d/%m/%y')  # ano minúsculo
hoje_formatado3 = hoje.strftime('%d/%M/%Y')  # mês e ano maíusculo
hoje_formatado4 = hoje.strftime('%D/%m/%Y')  # dia e ano maíusculo
hoje_formatado5 = hoje.strftime('%d/%B/%Y')  # mês binário maíusculo e ano maíusculo
hoje_formatado6 = hoje.strftime('%d/%b/%Y')  # mês binário minúsculo e ano maíusculo

print(hoje_formatado)
print(hoje_formatado2)
print(hoje_formatado3)
print(hoje_formatado4)
print(hoje_formatado5)
print(hoje_formatado6)