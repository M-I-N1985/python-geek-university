"""
filter() - serve para filtrar uma determinada coleção

"""
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Equador', '', 'Colombia', '', 'Venezuela']

filtro = filter(None, paises)
print(list(filtro))

filtro = filter(lambda pais: len(pais) > 0, paises)
print(list(filtro))



