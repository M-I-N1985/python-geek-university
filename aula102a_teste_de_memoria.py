"""
Teste de Memória com Generators

# Sequência de Fibonacco

1, 1, 2, 3, 5, 8, 13

"""

def lista_fib(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

print(lista_fib(10))
for n in lista_fib(100):
    print(n)