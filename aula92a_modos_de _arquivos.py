"""
r ->
w ->
x -> abre para escrita somente se o aarquivo não existir; caso o arquivo exista gerará um FileExistsError, podemos neste caso tratar com try
a ->

http://docs.python.org/3/library/functions.html#open
"""
try:
    with open('Univerity.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')
