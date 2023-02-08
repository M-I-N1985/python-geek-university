"""
criando um iterador semelhante a:

for i in range(1, 61)
    print(i)

"""

class Contador:
    def __init__(self, menor, maior):
        self.maior = maior
        self.menor = menor

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for n in Contador(1, 61):
    print(n)

