"""
Trabalhando com deltas de data e hora (diferenças entre data e hora)

data_inicial - dd/mm/yyyy 09:17:18.939329
data_final   - dd/mm/yyyy 11:07:36.846966

delta = data_final - data_inicial

"""

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)