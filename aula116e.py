"""
Metodo Estático

resumindo diferencas:
- Metodo de Instancia: Acesso a instancia
- Metodo de Classe: Acesso a classe do objeto
- Método Estático: Não tem acesso a classe nem a instancia
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # rounds = 200.000 embaralhamentos para gerar a senha. salt = tamanho da senha criptografada, para dificultar mais.
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # compara a senha digitada com a senha criptografada
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    def __gera_usuario(self):
        return self.__email.split('@')[0]

# Método Estático


print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user.contador)

print(user.definicao())
