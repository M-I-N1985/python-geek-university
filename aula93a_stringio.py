"""
StringIO

Atenção: para ler ou escrever em arquivos do sistema operacional o software precisa ter permissão de:
- Leitura
- Escrita

StringIO -> utilizada para ler e criar arquivos na memória.

"""

# Primeiro fazemos o import

from io import StringIO

mensagem = "Esta é apenas uma msg normal \n"

# podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois:
arquivo = StringIO(mensagem)
# arquivos = open('mensageml.txt', 'w')

# podemos manusea-lo normalmente
print(arquivo.read())

# escrevendo outros textos
arquivo.write('Outra msg')

# podemos inclusive movimentar cursos
arquivo.seek(0)
print(arquivo.read())