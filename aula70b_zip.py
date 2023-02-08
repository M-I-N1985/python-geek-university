"""
zip() Cria um iterável(zip object) que agrega elementos de cada um dos iteráveis com entrada em pares
"""
# podemos usar iteráveis diferentes com zip

tupla = 1, 2, 3, 4
lista = [5, 6, 7, 8]
dic = {'a': 9, 'b':10, 'c':11, 'd':12}

zt = zip(tupla, lista, dic.values())
print(list(zt))


# lista de tuplas
dados = [(0, 1), (1, 2), (2, 3)]
print(list(zip(dados))) # observe que eles fazem um desempacotamente item[i] com item [i]

