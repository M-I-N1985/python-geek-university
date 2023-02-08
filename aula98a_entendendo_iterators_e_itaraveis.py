"""
Entendendo Iterators e Iteráveis

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iteráveis ->
    - Um objeto que irá retornar um iterador quando a função iter() for chamada.


"""

nome = 'Geek'  # iterable
it = iter(nome)
print(next(it))
print(next(it))
