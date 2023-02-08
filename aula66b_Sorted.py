"""
Não confunda com a função sort(), pois este só funciona em listas

Podemos utilizar sorted() para qualquer iterável

Com sort() a lista original é alterada, mas com sorted, é gerado uma nova lista

OBS: QUANDO O ITERAVEL FOR UM DICIONARIO TEREMOS QUE INFORMAR O KEY PARA ORDENAÇÃO

"""

# Podemos usar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'Iuri', 'tweets': ['Eu adoro bolos', ' Eu adoro pizzas']},
    {'username': 'Taína', 'tweets': []}, {'username': 'Lucas', 'tweets': ['Hoje vai ser loco']},
    {'username': 'Guilherme', 'tweets': ['Vai corinthias']},
    {'username': 'Huayra', 'tweets': []},
    {'username': 'Ana', 'tweets': ['Quem roubou meu queijo', ' O bicho tá pegando!']}
]
print(usuarios)

# ordenando pelo username - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))  # para dicionarios fazemos uma funlçao pois para filtrar teria que ser item por item

# ordenando pelo numero de tweets - do maior para o menor
print(sorted(usuarios, key= lambda usuario: len(usuario['tweets'])))


