"""
DictiWriter
arquivo.writehead()
arquivo.writerow

"""

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()  # escreve no cabeçalho
    filme = None
    while filme != 'sair':
        filme = input('Qual o nome do filme: ')
        if filme != 'sair':
            genero = input('Qual o nome do Gênero: ')
            duracao = input('Qual o nome do Duração: ')
            escritor_csv.writerow({"Título":filme, "Gênero": genero, "Duração": duracao})  # escreve nas linhas
