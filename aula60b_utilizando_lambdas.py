"""
expressões Lambdas são funções anonimas.


obs: se passarmos mais argumentos do que parametros esperados teremos type error
"""

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('angelina', 'JOLIE'))
print(nome_completo(' Felipe ', '         jones           '))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

# lambda vai item a item da lista e separar os itens por espaço (split(' '))
# selecionar o ultimo item [-1] e colocar letras em minúscula

autores.sort(key= lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)