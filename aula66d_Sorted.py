"""
Não confunda com a função sort(), pois este só funciona em listas

Podemos utilizar sorted() para qualquer iterável

Com sort() a lista original é alterada, mas com sorted, é gerado uma nova lista

"""

musicas = [
    {'titulos': 'Thunderstruck', 'Tocou': 3},
    {'titulos': 'Dead Skin Mask', 'Tocou': 4},
    {'titulos': 'Back in Black', 'Tocou': 32},
    {'titulos': 'Too Old to Rock"in"roll, to ynoung to die', 'Tocou': 2}
]

# Ordenar da menos tocada para a mais tocada
# Como fazer isso sem usar max(), min()?

# maneira que o professor desenvolveu
max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['titulos'])

