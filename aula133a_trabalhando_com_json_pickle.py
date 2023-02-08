"""
JSON - JavaScript Object Notation

API - são meios de  


ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])  # dumps faz uma formatação padrão para o formato json
print(type(ret))
print(ret)

"""

import json

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__) # dumps faz uma formatação padrão para o formato json
print(ret)
