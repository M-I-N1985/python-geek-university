"""
Como os modulos python são arquivos python, então todos os arquivos criados até o momento são modulos
python prontos para serem utilizados

"""

from aula61b_map import cidades, c_para_f

print(list(map(c_para_f, cidades)))