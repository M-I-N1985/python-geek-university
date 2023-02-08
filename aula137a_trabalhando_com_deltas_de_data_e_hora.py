"""
Trabalhando com deltas de data e hora (diferenças entre data e hora)

data_inicial - dd/mm/yyyy 09:17:18.939329
data_final   - dd/mm/yyyy 11:07:36.846966

delta = data_final - data_inicial

"""

import datetime


# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2023, 12, 23, 0)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas...')
