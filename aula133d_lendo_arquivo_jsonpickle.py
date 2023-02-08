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

with open('felix.json', 'r') as arquivo:  # abrindo em modo leitura o arquivo com nome felix
    conteudo = arquivo.read()  # lê e coloca o conteudo de um arquivo em uma variavel
    ret = jsonpickle.decode(conteudo)  # decodificando o objeto felix no forma jsonpickle
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
