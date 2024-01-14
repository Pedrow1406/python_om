"""
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamentee as instâncias da classe com os dados salvos.
Faça em arquivos separados.
"""
import json
import os
class Pessoas():
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoas('Pedrow', 18)
pessoa2 = Pessoas('Maria', 15)
pessoa3 = Pessoas('João', 17)

lista_pessoas = [vars(pessoa1), vars(pessoa2), vars(pessoa3)]
caminho_pai = os.path.dirname(__file__)
CAMINHO_FILE = os.path.join(caminho_pai,'ex_aula206.json')

if __name__ == '__main__':
    with open(CAMINHO_FILE, 'w', encoding='utf8') as file:
        print('Fazendo Dump')
        json.dump(lista_pessoas, file, indent=2, ensure_ascii=False)
        
