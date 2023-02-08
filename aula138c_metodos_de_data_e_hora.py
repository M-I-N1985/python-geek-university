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


aniversario = input('Qual a sua data de nascimento? (dd/mm/yyyy) ')

aniversario = aniversario.split('/')
print(aniversario)

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu numa segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu numa terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu numa quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu numa quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu numa sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu num sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu num domingo')
