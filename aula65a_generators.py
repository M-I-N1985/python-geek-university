"""
Generators (ocupa menos recurso em memória)

vimos LC, DC, SC e agora vamos ver generators(seria como tuple comprehension)

"""
# Poderiamos ter feito os exemplos anteriores utilizando generators

nomes = ['Carlos', 'Camila', 'Cassiano']
print(any([nome[0] == 'C' for nome in nomes]))
print()

print(any(nome[0] == 'C' for nome in nomes))

# list comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)

# generators
res = (nome[0] == 'C' for nome in nomes)
print(res)

# fazendo um casting em um generators
res = tuple(nome[0] == 'C' for nome in nomes)
print(res)