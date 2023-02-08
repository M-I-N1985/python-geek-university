
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contado = self.__numero

class Produto:

    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto"""
        return(self.__valor * (100 - porcentagem)) / 100

# ir no Terminal e instalar a biblioteca passlib
# pip passlib
# caso não tenha sucesso clique (windows) em crtl+alt+S e selecione o projeto que vc está
# depois vai em Python interpreter (pode aparecer como project interpreter), depois
# vá em "+" e add a biblioteca desejada.

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # rounds = 200.000 embaralhamentos para gerar a senha. salt = tamanho da senha criptografada, para dificultar mais.

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # compara a senha digitada com a senha criptografada
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
