"""
Quando tratar um código?

"TODA A ENTRADA DE UM USUÁRIO DE SER TRATADO"

OBS: A função do usuário é destruir seu sistema

"""

Num = 0
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorretor')
else:
    print(f'Você digitou {num}')  # else é executado se não entrar em nenhuma exceção
finally:
    print('Executando o finally')  # sempre é executado

# OBS: Geralmente o finally é utilizado para fechar recurso