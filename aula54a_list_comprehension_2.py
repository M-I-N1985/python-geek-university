"""
Podemos adicionar estruturas condicionais logicas as nossas list comprehension

"""

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando

# Qualquer numero par módulo de 2 em python é 0, ou booleanamente falando, é False. O contrário True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

resultado = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(resultado)