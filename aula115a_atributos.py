"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nos conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instancia;
    - Atributos de Classe;
    - Atributos Dinâmicos;

#  Atributos de instancia: são atributos declarados dentro do método consturtor

#  OBS: Método contrutor = É um método especial utilizado para a construção de objetos

#  Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos assim:

public class Lampada(){
    private int voltagem;
    privat String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
        }
}

class Produto:

    def __init__(self, nome, descricao, valor):  # Método (construtor)
        self.nome = nome                         # Atributos nome do objeto Produto
        self.descricao = descricao               # Atributos descricao do objeto Produto
        self.valor = valor                       # Atributos valor do objeto Produto


#  atributos de instancia podem ser publicos ou privados
#  quando falamos publico ou privado, nos referimos a visibilidade
#  em Python, por convencao, ficou estabelecido que, todo atributo de uma classe é publico.
#  ou seja, pode ser acessado em todo o projeto
#  Caso queiramos demonstrar que detrerminado atributoo deve ser tratado como pribado, ou seja,
#  que deve ser acessado/ultilizado somente dentro da probria classe onde esta delcarado,
#  utiliza-se duplo undescore "__" no inicio de seu nome.

#  Isso é conhcedi tambem como Name Mangling.

# Atributos Publicos

#  Atributos Privados "self.__xxx"


"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.__ligada = False  #  'Lampada' "nasce" apagado, e desta forma não precisamos receber este valor durante a instanciação do objeto
                               #  Não existe uma obrigação que um atributo de inst. receba um parametro
class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


#  OBS: lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai
#  impedir que façamos acesso aos atributos sinalizados com privado fora da classe.

#  Exemplo

user = Acesso('user@gmailcom', '123456')

print(user.email)

print(dir(user))

# Acesso ao atributo pela classe (errado)
print(user._Acesso__senha)  #  Name Mangling temos acesso mas nao deveriamos fazer dessa maneira

#  print(user.__senha) #AtributeError

# Acesso ao atributo pelo método (correto)
user.mostra_senha()

#  O que significa atributo de instancia?
#  Significa que ao criarmos instancias/objetos de uma classe todas as instancias terão esses atributos.
#  Ou seja, cada instancia criada tera seus proprios valores

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()