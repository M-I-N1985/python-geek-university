"""
PEP8 - Python Enhancement Proposal - "Proposta de melhoria do linguagem
Boas praticas - no site do Python podemos procurar size Python -> Pep Index

1 - utilize Camel Case para criar classes;
2 - utilize nomes em minusculo separados por underline para funções ou variáveis;
3 - utilize 4 espaços para identação
4 - linhas em branco
    - separar funções e definições de classe com duas linhas em brando;
    - métodos dentro de uma classe devem ser separados com uma unica linha em branco;
5 - imports devem ser sempre feito em linhas separadas (não há necessidade de ter linha em branco neste caso
6 - espaço em expressoes e intruções:

    # não faça:
    funcao( algo[ 1 ],{ outro: 2 } )
    algo (1)
    dict ['chave'] = lista [indice]

    # faça
    funcao(algo[1],{outro: 2})
    algo(1)
    dict['chave'] = lista[indice]
7 - termine sempre uma instrução com uma nova linha
8 - comentarios simples com #, e comentario com mais de uma linha com aspas tripas.


obs1 - O Pycharme avisa quando não estivermos seguindo a pep8, por exemplo:  duas
linhas em branco após docstrings

obs2 - não é recomendado utilizar tab pois em alguns computadores o Tab pode ser
midificado para mais espaços

obs3: imports devem ser colocados no topo do arquivo, logo após os comentários ou docstrings
e antes de constantes ou variáveis globais

obs4: caso haja necessidade de importar mais funções dentro de uma classe, poderemos fazer:

from types import (
    StringType
    ListType
    SetTyoe
    ...
)

"""

import this