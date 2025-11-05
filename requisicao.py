import requests
import json


def personagens():
    url = 'https://last-airbender-api.fly.dev/api/v1/characters'

    # resquisição geral com parâmetros de paginação e filtro por nome
    params = {
        'page': 1,
        'perPage': 20,
        #'name': 'Aang'  # exemplo de filtro por nome
    }

    resultado = requests.get(url=url, params=params)

    print(json.dumps(resultado.json(), indent=4))

personagens()