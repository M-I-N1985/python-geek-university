"""
Assertions (Afirmações/Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simpres afirmações utilizadas nos testes.

Utilizamoso 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma msg de erro personalizada

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos testes.

# OBS: Existe uma flag que ocasiona em uma falha na palavra reservada Assertios, ex:
Escrevendo no terminal:
    python -O aula142b_assertions_afirmacoes.py #que é o nome do arquivo, não funcionará.


"""


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))