"""
Conhemdo o Piclke

"Regra geral - nunca abrir um arquivo pickle desconhecido, ou de origem desconhecida"

Os dados são salvos em formato binário (Hexadecimal) - um conversor

serializaçõa/deserialização

"""

import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'O {self.__nome} está comendo!')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'O {self._Animal__nome} está miando')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'O {self._Animal__nome} está latindo')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a escrita em arquivos pickle

with open('animais.pickle', 'wb') as arquivo:  # wb - escrita binária
    pickle.dump((felix, pluto), arquivo)