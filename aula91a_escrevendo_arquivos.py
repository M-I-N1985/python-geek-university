"""
Escrevendo em arquivos

Ao abrir um arquivo para escreta, o arquivo e criado no sistema operacional.

A função write() precisa receber uma string como parametro. Caso não receba, teremos um TypeError

Abrindp um arquivo no modo escrita, caso o arquivo não exista ele será criado. Caso ele exista,
a informação nova será reescrita em cima da anterior que será apagada.



"""


# Modo Pythonico

with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Novos dados. \n')
    arquivo.write('podemos colocar quantas linhas quisermos. \n')
    arquivo.write('mas esta será a ultima linha. \n')
