"""
# Para fixar - Map
# Temos dados iteráveis
# dados: a1, a2, a3 .., an
# Temos uma função:
# função: f(x)
# Utilizamos a função map(f, dados) onde map ira mapear cada elemento dos dados e aplicar a função



"""

# Mais um exemplo (uma lista de cidades com temperaturas em graus celcius

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19)]
print(cidades)

# Como cconverter para fareheith
# f = 9/5 * c + 32
# usando o lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

