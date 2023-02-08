"""
filter() - serve para filtrar uma determinada coleção

OBS: Diferença entre filter e map

# map() - Recebe dois parâmetros, uma função e um iterável e retorna um objeto
mapeando a função para cada elemento do iterável.

# filter() - Recebe dois parâmetros, uma função e um iterável e retorna um objeto
filtrando apanas os elementos de adordo com a função. (é praticamente um funçao booleana)




"""# Exemplos mais complexos
usuarios = [
    {'username': 'Iuri', 'tweets': ['Eu adoro bolos', ' Eu adoro pizzas']},
    {'username': 'Taína', 'tweets': []}, {'username': 'Lucas', 'tweets': ['Hoje vai ser loco']},
    {'username': 'Guilherme', 'tweets': ['Vai corinthias']},
    {'username': 'Huayra', 'tweets': []},
    {'username': 'Ana', 'tweets': ['Quem roubou meu queijo', ' O bicho tá pegando!']}
]

print(usuarios)
print('')

# Filtrando usuários inativos no twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)
print('')

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)
print('')