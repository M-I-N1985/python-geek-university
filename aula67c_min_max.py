"""
max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos
min() -> idem max()
"""

# Exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'Tocou': 3},
    {'titulo': 'Dead Skin Mask', 'Tocou': 2},
    {'titulo': 'Back in Black', 'Tocou': 4},
    {'titulo': 'Too Old to Rock"in"roll, to ynoung to die', 'Tocou': 32}
]

print(max(musicas, key=lambda musica: musica['Tocou']))
print(min(musicas, key=lambda musica: musica['Tocou']))

# Como imprimir só o titulo?
# Versão do professor:
print(min(musicas, key=lambda musica: musica['Tocou'])['titulo'])

# minha resolução:
mais_tocada = max(musicas, key=lambda musica: musica['Tocou'])
print(mais_tocada['titulo'])