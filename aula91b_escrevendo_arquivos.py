"""
Escrevendo em arquivos

Ao abrir um arquivo para escreta, o arquivo e criado no sistema operacional.

A função write() precisa receber uma string como parametro. Caso não receba, teremos um TypeError

Abrindp um arquivo no modo escrita, caso o arquivo não exista ele será criado. Caso ele exista,
a informação nova será reescrita em cima da anterior que será apagada.



"""


# Modo tradicional

arquivo = open('mais novo.txt', 'w', encoding='utf-8')
arquivo.write('blablabla. \n')
arquivo.write('kkkkkkk. \n')
arquivo.write('xiiiii, silêncio!. \n')

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)