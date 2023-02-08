"""
reduce() não é mais uma função integrada, a partir do python3. temos que importar o
módulo 'functools'

Guido van Rossum: Utilize a função reduce() somente se vc realmente precisar dela. Em 99% das vezes
um loop for é mais legível

seria uma espécie de função composta (em matemática)

Para entender reduce():
# Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3,..., an]

# E você tem uma função que receba dois parâmetros:

def funcao(x, y):
     return x * y

assim com map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

a função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    passo 2: res2 = f(res1, a3) # aplica a função passando o resulatado do passo 1 mais o terceiro elemento e guarda o resultado

    Isso é repetido até o final.
    passo 3: res3 = f(res2, a4)
    .
    .
    .
    passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o
resultado da aplicação anterior. No final, reduce() ira retornar o resultado final.

seria uma espécie de função composta (em matemática)
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 8, 11, 17, 19, 23, 29]


multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

res = 1
for dado in dados:
    res = res * dado
print(res)