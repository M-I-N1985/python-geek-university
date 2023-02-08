"""
#  Atributos de Classe


#  Atributos de classe são atributos, claro, que são  declarados diretamente na classe, ou seja
#  fora do construtor. Geralmente já inicializamos um valor e este valor é compartilhado entre
#  todas as instancias da classe. Ou seja, ao inves de cada instancia da classe ter seus proprios
#  valores como é o caso dos atributos de instancia, com os atrinutos de classe todas as instancias
#  terão os mesmo valores para este atributo.

"""

#  Refatorando a classe Produto

class Produto:

    #Atributo de classe
    imposto = 1.05  # 0,05% de imposto
    contador = 0

    #  observe que o id é um atributo de instancia, não é
    #  obrigatório que a funcao abaixo receba este atributo.
    #  Note que ele se implementa apartir do atributo de classse "contador".


    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1   #  Não existe uma obrigação que um atributo de inst. receba um parametro, nesse caso ele recebeu diretamente da classe
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id  # Atributo de classe = Nomedaclasse.nomedoatributo

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possivel, mas incorretor de um atributo de classe
print(p2.valor)  # Acesso possivel, mas incorretor de um atributo de classe

#  OBS: Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)


#  OBS: Em Java os atributos conhcecidos aqui como atributos
#  de classe, em Python, são chamados de atributos estáticos.

#  Atributos dinamicos -> um atributo de instancia que pode ser criado em tempo de execução

#  OBS: O atributo dinâmico sera exclusivo da instancia que o criou.


p1 = Produto('Playstation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso
                 # Ele está sendo criado na instância do objeto

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

#  como não existe o atributo peso para p1 então não conseguimos ir adiante no exemplo abaixo
#  print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)  # __dict__ Devolve para gente um dicionario com os atributos
print(p2.__dict__)
# print(Produto.__dict__)


#  assim com é possivel adicionar atributos dinamicamente, também é possivel remover
del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)  # __dict__ Devolve para gente um dicionario com os atributos
print(p2.__dict__)