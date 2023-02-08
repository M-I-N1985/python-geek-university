"""
raise -> lanca exceções
"é uma palavra reservada, como def"

OBS1: serva para lançarmos nossas proprias exceções nas mensagens de erro
Ex:
    raise ValueError('Valor incorreto')

OBS2: não é tratamento de erro, mas sim lancçamento de erros
OBS3: Assim como return ele finaliza a função

"""

def colore(texto, cor):
    cores = ('Branco', 'Azul', 'Vermelho')
    if type(texto) is not str:
        raise TypeError(f'A palavra {texto} precisa ser uma string')
    if type(cor) is not str:
        raise TypeError(f'A cor {cor} precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa estar entre as cores: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek University', 'Azul')
