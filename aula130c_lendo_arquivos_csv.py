"""
Como usar o DictReader


o separador do Dictreader default é "," então nos casos que o separador for outro teremos que destaca-lo

- No caso do separador ser ";" então a função ficaria assim: DictReader(arquivo, delimiter=";")
"""
#  DictReader

from csv import DictReader

with open('lutadores.csv', encoding ='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)  # segura crtl e clica no reader para ter especificações

    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')




    
