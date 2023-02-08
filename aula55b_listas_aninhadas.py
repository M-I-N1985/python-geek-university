"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes)

    Em Python nós temos listas
numeros = [1, 'b', 3.234, True]
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3x3

[[print(num) for num in lista] for lista in listas]

# Gerando um tabuleiro de Xadrez
tabuleiro = [[num for num in range(1, 4)] for lista in range(1, 4)]
print(tabuleiro)
print('')

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
print('')

# Gerando valor iniciais

print([["*" for i in range(1, 4)] for j in range(1, 4)])