"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

#  Separador por vírgula

1, 2, 3, 4, 5, 6
"""

'''
"geek", "universidade", "python", "ciência", "dados"

#  Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "universidade"; "python"; "ciência"; "dados"

#  Separador por espaço

1 2 3 4 5 6

"geek" "universidade" "python" "ciência" "dados"

http://dados.gov.br/dataset
'''
#  no meu pc eu tive que detalhar o encofing = utf-8 pois no ex. do professor deu erro UnicodeDecodeError
#  Possivel de se trabalhar, mas não é o ideal
with open('lutadores.csv', encoding ='utf-8') as arquivo:
    dados = arquivo.read()
    print(dados)
    #print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

