"""
Quando tratar um código?

"TODA A ENTRADA DE UM USUÁRIO DE SER TRATADO"

OBS: A função do usuário é destruir seu sistema

"""

# Exemplo + Complexo

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')
print(dividir(num1, num2))
