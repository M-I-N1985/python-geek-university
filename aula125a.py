"""
POO - MRO - Method Resolution Order (Resolução de Ordem de Métodos),
é a ordem de execução dos métodos (quem será executado primeiro).

Em Python podemos conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedades da classe __mro__
    - Via método mro()
    - Via help

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

pinguim = Pinguim('Tux')
print(pinguim.cumprimentar())


#  Testando
# Pinguim(Terrestre, Aquatico)
# Eu sou Tux do mar!
#
# Pinguim(Aquatico, Terrestre)
# Eu sou o Tux da terra!

# No Python Console
# from aula123a import Pinguim
# Pinguim.__mro__
# Pinguim.mro()
# help(Pinguim)


