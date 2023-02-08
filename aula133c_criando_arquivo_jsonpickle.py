"""
JSON - JavaScript Object Notation

integrando o JSON com o Pickle

pip install jsonpickle

"""

import jsonpickle

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

with open('felix.json', 'w') as arquivo:  # criando um arquivo com nome felix
    ret = jsonpickle.encode(felix)  # codificando o objeto felix no forma jsonpickle
    arquivo.write(ret)  # escrevendo o arquivo codificado no arquivo felix
