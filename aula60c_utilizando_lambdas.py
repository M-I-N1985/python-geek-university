"""
expressões Lambdas são funções anonimas.

"""

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

func = lambda sobrenome: sobrenome.split(' ')[-1].lower()

print(func('Isaac Asimov'))

# montando uma lista com os sobrenomes
print([func(sobrenome) for sobrenome in autores])

