
import aula85b_primeiro


def funcao2():
    aula85b_primeiro.funcao1()


if __name__ == "__main__":
    funcao2()
    print('segundo.py está sendo executado diretamente')

else:
    print('segundo.py foi importado.')
