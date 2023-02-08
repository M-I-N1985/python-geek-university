"""
Erros mais comuns

1 - SyntaxError  # foi escrito algo que não é proprio da linguagem
exemplos:
    a) def funcao:
        print('x')
    b) None = 1
    c)
        return
2 - NameError  # variavel ou funcao nao foi definida
exemplos:
    a) print(geek)
    b) geek()

3 - TypeError  #  funcao/operacao/acao é aplicada a tipos errados
exemplos:
    a) print(len(5))  # a função len funciona com iteráveis somente.
    b) print('geek' + [])

4 - IndexError  # quando tentamos indexar um elementeo da lista que estrapola o indice
exemplos:
    a) lista = ['Geek']
       print(lista[0][10])

5 - ValueError  # função ou operação built-in recebe um argumento correto + o valor é inapropriado
exemplos:
    a)print(int(geek))

6 - KeyError  # acessar um dicionário com chave errada
7 - AttributeError  # Quando uma variável não tem atributo/função
exemplos:
    tupla = (1, 2, 3, 4)
    print(tupla.sort())  # função sort() é dif de sorted(), ou seja, ela só aceita lista
    
8 - IndentationError







"""