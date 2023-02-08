"""
Função readline ==> lê o arquivo linha a linha



"""


arquivo = open("aula88texto.txt", 'r', encoding='utf-8')

print(arquivo.readline())

print(arquivo.readline())

print(arquivo.readline().split(' '))
