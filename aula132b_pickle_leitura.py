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

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'O {self.__nome} está comendo!')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'O {self.nome} está miando')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'O {self.nome} está latindo')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a leitura em arquivos pickle

with open('animais.pickle', 'rb') as arquivo:  # wr - escrita binária
    gato, cachorro = pickle.load(arquivo)
    # Acessando da maneira incorreta
    # print(f'O gato chama-se {gato._Animal__nome}')
    # gato.mia()
    # print(f'O tipo do gato é {type(gato)}')
    #
    # print(f'O gato chama-se {cachorro._Animal__nome}')
    # cachorro.mia()
    # print(f'O tipo do gato é {type(cachorro)}')

    # para acessar da maneira certa tive que criar @propertie

    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O gato chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do gato é {type(cachorro)}')