"""
POO - Métodos Mágicos

São todos os métodos que utilizam dunder.
dunder init -> __init__()

Dunder > Double Underscore
dunder repr > Representação do objeto
def __repr__(self):
    return f'{self.__titulo} escrito por {self.__autor}'

ir em Python Console e importar esta aula e o objeto livro

from aula127a.... impor Livro

Python Rocks
l1 = Livro('Qualquer', 'Outro', 455)
print(l1)
Qualquer
print(str(l1))
Qualquer
print(repr(l1))

"""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    # O objeto len abaixo é diferente, pois é necessário contar uma quantidade de letras
    # def __len__(self):
    #     return len(self.__titulo)

    def __del__(self):
        print(f'Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, other):
        return f'{self.__autor} - {other.__autor}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ""
            for n in range(other):
                msg += " " + str(self)
            return msg
        return 'Não posso multiplicar pois o segundo item não é um numero inteiro'


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(repr(livro1))
print(len(livro1))
#  Operações com instâncias
print(livro1 + livro2)
print(livro1 * 3)