"""
r ->
w ->
x -> abre para escrita somente se o aarquivo não existir; caso o arquivo exista gerará um FileExistsError, podemos neste caso tratar com try
a -> abre para escrita adicionando conteudo caso o arquivo já exista. (se o arquivo não existir, será criado)


"""
with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
