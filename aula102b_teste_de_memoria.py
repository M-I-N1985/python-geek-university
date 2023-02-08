"""
Teste de Memória com Generators

Usando Generator o espaço poupado em momório pode chegar a 50x

# Sequência de Fibonacco

1, 1, 2, 3, 5, 8, 13

"""

def gerador_fib(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

print(gerador_fib(10))
for n in gerador_fib(100):
    print(n)