"""
Teste de velocidade com expressões geradoras

"""
#realizando o teste de velocidade

import time

# Generator expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'O tempo de espera no Generator Expression levou {gen_tempo}')
print(f'O tempo de espera na List Comprehension levou {list_tempo}')