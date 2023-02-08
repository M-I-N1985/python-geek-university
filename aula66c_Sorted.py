"""
Não confunda com a função sort(), pois este só funciona em listas

Podemos utilizar sorted() para qualquer iterável

Com sort() a lista original é alterada, mas com sorted, é gerado uma nova lista

"""

musicas = [
    {'titulos': 'Thunderstruck', 'Tocou': 3},
    {'titulos': 'Dead Skin Mask', 'Tocou': 2},
    {'titulos': 'Back in Black', 'Tocou': 4},
    {'titulos': 'Too Old to Rock"in"roll, to ynoung to die', 'Tocou': 32}
]

# Ordenar da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['Tocou']))

# Ordenar da mais tocada para a menos tocada

print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))
