"""
filter() - serve para filtrar uma determinada coleção

OBS: Diferença entre filter e map

# map() - Recebe dois parâmetros, uma função e um iterável e retorna um objeto
mapeando a função para cada elemento do iterável.

# filter() - Recebe dois parâmetros, uma função e um iterável e retorna um objeto
filtrando apanas os elementos de adordo com a função. (é praticamente um funçao booleana)




"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de alguma fonte
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')

# Assun como map(), filter() recebe dois parametros sendo o primeiro uma função e
# o segundo um iteravel


filtro = filter(lambda valor: valor > media, dados)
print(type(filtro))
print(list(filtro))

# assim como na função map(), após ser utilizado so dados de filter(0 els são excluidos da memória
