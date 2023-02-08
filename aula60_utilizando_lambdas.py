"""
expressões Lambdas são funções anonimas.

"""
# função comum

def soma(a, b):
    return a + b

# Expressão Lambda

lambda a, b: a + b

# como utilizar a expressão lambda?
# vc atribui ela a uma variável

calc = lambda a, b: a + b
print(calc(4,2))
