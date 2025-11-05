import requests
import json
from googletrans import Translator


def traduzir(texto):
    # Verifica se o texto é válido antes de traduzir
    if not texto or texto.strip() == '':
        return texto  # Retorna o texto original se for vazio ou None
    
    translator = Translator()
    traducao = translator.translate(texto, dest='pt')
    return traducao.text

def personagens():
    url = 'https://last-airbender-api.fly.dev/api/v1/characters'

    # resquisição geral com parâmetros de paginação e filtro por nome
    params = {
        'page': 1,
        'perPage': 10,
        #'name': 'Aang'  # exemplo de filtro por nome
    }

    personagens = requests.get(url=url, params=params).json()

    # traduzindo atributos específicos - name e affiliation
    for personagem in personagens:

        name = personagem.get('name', '')
        affiliation = personagem.get('affiliation', '')
        if name:
            personagem['nome'] = traduzir(name)
        if affiliation:
            personagem['afiliacao'] = traduzir(affiliation)

    print(json.dumps(personagens, indent=4, ensure_ascii=False))


personagens()