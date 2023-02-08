"""
filter() e map()



"""
nomes = ['Vanessa', 'Ana', 'Lucia']

# devemos criar uma lista contaendo "Sua instrutora é", + nome,
# desde que cada nome tenha pelo menos 5 caracteres.

# observe abaixo que o filter está dentro de map, pois
# como map retorna um valor, e filter retorna um iterável filtrado.
lista = list(map(lambda nome: f'Sua intrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)