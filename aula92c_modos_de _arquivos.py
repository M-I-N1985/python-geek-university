"""
r ->
w ->
x -> abre para escrita somente se o aarquivo não existir; caso o arquivo exista gerará um FileExistsError, podemos neste caso tratar com try
a -> abre para escrita adicionando conteudo caso o arquivo já exista. (se o arquivo não existir, será criado)
obs: o conteudo será add no final do arquivo, sempre, ou seja, não controlamos o cursor!
+ -> abre para o modo de atualização, leitura e escrita.
obs: essa explicação do professor foi bem ruim, pois não explicou muito a diferenção entre '+' e 'a'
obs2: a diferença entre '+r' e 'r' é que a primeira, vc pode selecionar onde vc vai inserir.
e a segundo sobrescreve todo o arquivo.
"""


with open('novo2.txt', 'r+', encoding='utf-8') as arquivo:

