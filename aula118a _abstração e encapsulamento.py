"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierarquico
utilizando classes.

Encapsular - capsula

            classe
--------------------------------
|                              |
|       atributos e métodos    |
|______________________________|

# relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado chamado __falar()

esses elementos privados só devem/deveriam ser acessados dentro da classe.
Mas em Python não bloqueia este acesso fora da classe. Com Python acontece
um fenômeno chamado Name Mangling, que faz um alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo acessando elementos privados fora da classe:

instancia._Pessoa__nome  #Acessando atributo
instancia.Pessoa__falar()  #Acessando metodo

Abstração, em POO é o ato de expor apenas
dados relevantes de uma classe, escondendo atributos e metodos privados de usuário.

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

#  Testando acesso por fora da classe quando os dados estão escrito de forma publica)

conta1 = Conta('Geek', 150.00, 1500)
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 9999999999999999
conta1.limite = 99999999999999999999999999999999999

print(conta1.__dict__)
conta1.extrato()
