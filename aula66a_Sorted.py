"""
Não confunda com a função sort(), pois este só funciona em listas

Podemos utilizar sorted() para qualquer iterável

Com sort() a lista original é alterada, mas com sorted, é gerado uma nova lista

"""

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # ordena do menor para o maior

print(numeros) # permanece com os valores originais

print(sorted(numeros, reverse = True))  # Ordena do maior para o menor