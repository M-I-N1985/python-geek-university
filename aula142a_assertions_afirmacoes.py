"""
Assertions (Afirmações/Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simpres afirmações utilizadas nos testes.

Utilizamoso 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma msg de erro personalizada

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos testes.

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 4)  # 6
print(ret)
# ret2 = soma_numeros_positivos(-2, 4)  # AssertionError
# print(ret2)
