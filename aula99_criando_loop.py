string = 'Geek University'
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for(string)
meu_for(numeros)