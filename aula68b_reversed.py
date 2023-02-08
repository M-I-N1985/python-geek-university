"""
Não confundir reversed() com reverse()
reverse() pertence somente a listas
reverser() funciona com qualquer iterável

"""

# Outros exemplos

# fazendo o mesmo que reversed, com for
for letra in reversed('Iuri Nunes'):
    print(letra, end=' ')  # desta forarma ele imprime inteiro. Normalmente ele imprime
                           # letra a letra, mas isso porque o separador
                           # de linha (end) é implicito "\n"
print()

# pode fazer com joim
print(''.join(list(reversed('Iuri Nunes'))))

# com slice
print('Iuri Nunes'[ : : -1])

# reversed com for

for i in reversed(range(0, 10)):
    print(i)

