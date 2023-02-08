
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor inserido não pode ser negativo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')
        else:
            print('O valor inserido não pode ser negativo')

    def transferir(self, valor, conta_destino):
        #  1  - Remover o valor da conta de origem
        self.__saldo -= valor
        #  2  - adiciona o valor na conta destino
        conta_destino.__saldo += valor
#  Testando acesso por fora da classe quando os dados estão escrito de forma privada)
#  Name Mangling

conta1 = Conta('Geek', 150.00, 1500)


print(conta1.__dict__)

print(conta1._Conta__titular)
print(conta1._Conta__saldo)
print(conta1._Conta__limite)


conta1._Conta__numero = 42
conta1._Conta__titular = 'Xuxa'
conta1._Conta__saldo = 2500
conta1._Conta__limite = 50000

conta1.depositar(-150)  # veja que um depósito negativo seria um erro, então faz-se um "if" no metodo

print(conta1.__dict__)

conta1.sacar(3000)

print(conta1.__dict__)

#  transferindo de uma conta para a outra

conta1 = Conta('Angelina', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()
