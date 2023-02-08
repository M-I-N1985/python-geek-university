"""
Métodos de Classe em Python são conhcecidos com Métodos estáticos em outras liguagens
"""

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # rounds = 200.000 embaralhamentos para gerar a senha. salt = tamanho da senha criptografada, para dificultar mais.
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # compara a senha digitada com a senha criptografada
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreto


