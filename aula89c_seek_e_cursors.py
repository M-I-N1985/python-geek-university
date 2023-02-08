"""
Função readlines  ==>

OBS: Quando criamos ou abrimos um arquivo com a função open() é criado uma concexão 
entre o computador e a programa chamada streaming. Ao finalizar os trabalhas deveremos 
fechar essa concexão com chamado close()
Passos pasr se trabaçlhjar com um arquivo:
1 - Abrir o arquivo;
2 - Manipular o arquivo;
3 - Fechar o arquivo;
 
 """


# 1 - Abrir o arquivo:
arquivo = open("aula88texto.txt", 'r', encoding='utf-8')

# 2 - Trabalhar o arquivo:
print(arquivo.read())

print(arquivo.closed)

# 3 - Fechar o arquivo:
print(arquivo.close())

print(arquivo.closed)


