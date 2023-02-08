"""
expressões Lambdas são funções anonimas.

"""
# Função Quadrática =
# f(x) = a * x**2 + b * x + c

# definindo a função:
def func_quad(a, b, c):
    return lambda x: a * x**2 + b * x + c

# Podemos fazer assim:

teste = func_quad(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# ou podemos fazer diretamente:

print(func_quad(2, 3, -5)(0))
print(func_quad(2, 3, -5)(1))
print(func_quad(2, 3, -5)(2))
