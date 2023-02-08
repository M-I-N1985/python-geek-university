"""
Como usar o Reader

"""
#  Reader

from csv import reader

with open('lutadores.csv', encoding ='utf-8') as arquivo:
    leitor_csv = reader(arquivo)  # segura crtl e clica no reader para ter especificações
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')




    
