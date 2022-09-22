import json

def escrever_json(lista):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(lista, f, indent=4)