"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?
O parâmetro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis.


# Exemplos
def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros())


#  Entendendo o args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))

def imprime_o_que_tiver(nome1, nome2, *args):
    return args

print(imprime_o_que_tiver("Iuri", "Taina", 36))
print(imprime_o_que_tiver("Iuri", "vovozinha"))

def imprime_o_que_tiver2(*args):
    return args

print(imprime_o_que_tiver2("Iuri", "Taina", 36))


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info('Geek', 'University'))
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info())

"""

def soma_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

num1, num2, num3, num4, num5, num6, num7 = numeros

print(soma_numeros(num1, num2, num3, num4, num5, num6, num7))

#  exemplo onde *args substitui perfeitamente o exemplo acima, em poucas palavras

print(soma_numeros(*numeros))

#  OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento
#  uma coleção de dados. Desta forma ele sabera que precisara antes desempacotar estes dados.
#  OBS2: lembrando que isso funciona para coleções de dados(lista, tupla, set)
#  Para dicionário usa-se **kargs



