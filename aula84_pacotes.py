"""
Pacotes não é a mesma coisa que módulos, pois pacotes são uma pasta contendo diversos arquivos (módulos)

OBS: nas versões inferiores ao Python 2x, um pacote python deverá conter dentro dele um arquivo __init__.py, mas nas versões > 3x não é
obrigatório + ainda é util para compatibilidade.

Toda vez que um pacote é criado, automaticamente é criando um arquivo __init__.py

"""

from pacote_geek import geek1, geek2
from pacote_geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 6))
print(geek2.curso)
print(geek2.funcao2())
print(geek3.funcao3())
print(geek4.funcao4())