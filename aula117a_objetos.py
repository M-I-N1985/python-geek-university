"""
POO - Objetos são instancia da classe, ou seja, após o mapeamento do objeto do mundo real para
sua representação computacional, devemos poder criar quantos objetos forem necessários.
Podemos pensar
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):

        self.numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


lamp1 = Lampada('Vermelho', 220, 60)
print(f'Qual o estado da Lâmpada? {lamp1.checa_lampada()}')

cli1 = Cliente('Angelina Jolie', '008.164.240-71')
cc = ContaCorrente(5000, 10000, cli1)
cc.mostra_cliente()
cc._ContaCorrente__cliente.diz()
