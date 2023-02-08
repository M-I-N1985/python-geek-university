"""
Leitura de Arquivos

função open() - para abrir o conteudo de um arquivo


open() -> Passado somente um parametro de entrada (O caminho a ser lido)

Função retorna um _io (TextIOWrapper)

# obs: por padrão a função open abre o arquivo para leitura.
Este arquivo deve existir



#  Para ler o conteudo de um arquivo após sua abrtura, utilizamos a função read()

"""

#  Exemplo

arquivo = open('aula88texto.txt', 'r', encoding='utf-8')

print(arquivo)
print(type(arquivo))


ret = arquivo.read()
print(ret)
print(type(ret))

#  OBS: O Python utiliza um recurso chamado cursos, ou seja, a função read() lê
#  todo arquivo, até o final do cursor. Se tentarmos imprimir novamente nada aparecerá,
#   poi so cursor já está no final

print(ret.split(","))

