"""
utilizar o 'Terminal' e digitar python, quando quiser usar testar pedacos do codigo
ex:

terminal: soma.__name__
       R: 'soma'
Terminal: soma.__doc__
       R: 'Soma de dois números.'



"""

def ver_log(funcao):
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