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

ret = jsonpickle.encode(felix) # dumps faz uma formatação padrão para o formato json
print(ret)
