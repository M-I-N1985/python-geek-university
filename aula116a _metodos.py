"""
POO - Métodos

- Métodos (funções) => Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância
e Métodos de Classe

# Métodos de Instância

# o método dunder init "__init__" é um método especial chamado de construtor e sua
funçaõ é construir um objeto a partir do construtor

OBS: Os metodos/funcoes dunder em Python são chamsdos de métodos magicos.

Atenção: por mais que possamos criar nossas proprias funções utilizando dunder,
não é aconselhado. Phyton possui varios metodos com esta forma de nomeclatura
e pode ser que mudemos o comportamento dessa funcoes magicas interna da liguagem.
Então evite ao maximo ou então não o faça.

"""


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
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# p1 é a instancia
p1 = Produto("Playstaton 4", "Video Game", 2300)
print(p1.desconto(10))

# Não é possivel dar o desconto pela classe
# print(Produto.desconto(20))

print(Produto.desconto(p1, 40))  # self, desconto

user1 = Usuario('Iuri', 'Mesquita Nunes', 'iuri.mnunes@gmail.com', '123456')
user2 = Usuario('Taina', 'Vianna', 'tatynv@gmail.com', '456123')

print(user1.nome_completo())
print(user2.nome_completo())

# usando a classe para executar, preciso passar a instancia (self)
print(Usuario.nome_completo(user1))

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('senha não confere...')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # acesso errado
