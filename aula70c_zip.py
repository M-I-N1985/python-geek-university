"""
zip() Cria um iterável(zip object) que agrega elementos de cada um dos iteráveis com entrada em pares
"""
# exemplo mais complexo

prova1 = [80, 91, 78]

prova2 = [98, 89, 53]

alunos = ['Tainá', 'Iuri', 'José']

print(list(zip(alunos, prova1, prova2)))
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(dict(final))
print('')

# Podemos utilizar tbm o map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))