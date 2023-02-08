"""
Métodos de Data e Hora


# Encontrar o dia da semana. weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)

"""

import datetime


manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())
