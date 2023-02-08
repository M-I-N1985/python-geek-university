"""
#  Sobrescrita de Métodos (Overriding)

Sobrescrita de método o ocorre quando reescrevemos/ reimplementamos um método presente
na superclasse em uma classe ou em classes filhas.

"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)