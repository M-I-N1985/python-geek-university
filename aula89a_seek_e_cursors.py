"""
Função Seek ==> Movimenta o cursor para um ponto que inicia na quantidade de caracteres indicada.
Ex: arquivo.seek(20)




"""


arquivo = open("aula88texto.txt", 'r', encoding='utf-8')
print(arquivo.read())

# coloquei na quantidade de caracteres que iniciará a leitura
arquivo.seek(22)

# coloquei a quantidade de caracteres a ler
print(arquivo.read(22))


