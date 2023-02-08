"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes)

    Em Python nós temos listas
numeros = [1, 'b', 3.234, True]
"""

# Exemplos

listas= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3x3

print(listas)
print(type(listas))

# Como fazer acesso aos dados da lista

print(listas[0][2])
print(listas[2][-2])
print('')

# Iterando com loops em uma lista aninhadas
for lista in listas:
    for num in lista:
        print(num)