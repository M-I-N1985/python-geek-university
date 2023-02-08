#  Como corrigir o problema anterior?

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """ Eu sou uma funcao (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma de dois números."""
    return a + b

#  print(soma(10, 30))

print(soma.__name__)  # era para imprimir -> soma
print(soma.__doc__)  # era para imprimir ->  soma dois numeros

print(help(soma))