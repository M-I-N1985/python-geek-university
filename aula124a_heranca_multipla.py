"""
POO - Herança Múltipla

Herança Multipla é a possibilidade de uma classe herdar de multiplas classes.
Fazendo que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

#OBS: A herança multipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

    class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass

#  Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

OBS: Não importa se a derivação é direta ou indireta.
A classe que realizar a herança herdará todos os atributos
e metodos das super classes;
"""

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Olá eu sou {self.__nome}!'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'

    def cumprimentar(self):
        return f'Olá eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Olá eu sou {self._Animal__nome} da Terra!'

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

#  Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimentar())

#  Objeto é instância de ...

print(f'Tux é instância de Pinguim? {isinstance(pinguim, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(pinguim, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(pinguim, Terrestre)}')
print(f'Tux é instância de object? {isinstance(pinguim, object)}')

#  Qualquer classe é uma herança object
#  class Humano(object)