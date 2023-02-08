"""
len()
abs() - retorna um numero absoluto de um numero interiro ou tral
sum() - retorna um iterável podendo receber um inicial que por defaul é zero
round() - retorna um numero arredondado para 'n' digitos de precisão. Se 'n' não for
informado ele retornará o numero inteiro mais proximo da entrada

"""

# Len por debaixo dos panos é assim:
print('Iuri Nunes'.__len__())

print(abs(-5))
print(abs(-3.1415))

print(sum([1, 2, 3]))
print(sum([1, 2, 3]), -5)
print(sum({'a':1, 'b':2, 'c':3}.values()))

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(round(1.2199999, 2))
