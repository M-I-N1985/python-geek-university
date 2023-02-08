"""
Métodos de Data e Hora

para funcionamento das funções abaixo é necessário instalar:

- pip install textblob
- pip install googletrans
- pip install tk
"""

import datetime
from textblob import TextBlob


def formata_data(data):
    print(f"{data.day} de {data.strftime('%B')} de {data.year}")  # exemplo sem tradução
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(from_lang='en-us', to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))
