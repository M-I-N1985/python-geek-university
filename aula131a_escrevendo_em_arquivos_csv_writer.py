"""
importar a função writer

write
writerow([lista de variaveis])

abrir arquivos -> open('arquivo')
abrir para escrever -> open('arquivo', 'w') // se o nome do arquivo for o mesmo escreve em cima, se
não ele cria um novo arquivo

w - escreve
a - adiciona

"""

from csv import writer

with open('filmes.csv', 'w') as arquivo:  # cria um arquivo mas não salva
    escritor_csv = writer(arquivo)  # salva o arquivo em uma variável
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # escreve uma linha
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])






