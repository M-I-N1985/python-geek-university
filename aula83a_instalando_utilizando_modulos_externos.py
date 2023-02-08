"""
Utilizaremos o gerenciador de pacotes externos PIP - python installer package
http://pypi.org
# Podemos conhecer todos os pacotes essenciais

# Lá no terminal digite "pip install + nome do pacote"
# nessa aula foi instalado o pip install python-pdf que está no link abaixo:
https://pypi.org/project/python-pdf/

"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')

with open('test_doc.pdf', 'wb', encoding='utf-8') as f:
    f.write(pdf)