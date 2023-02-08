"""
Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Manipular o arquivo;
3 - Fechar o arquivo;

O Bloco With é o metodo Pythonico de se trabalhar pois
quando se sai dele o arquivo é fechado sem precisar
usar o recurso close()

"""
with open('aula88texto.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)