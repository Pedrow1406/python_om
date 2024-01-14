import json
from ex_aula206 import Pessoas, CAMINHO_FILE

with open(CAMINHO_FILE, 'r', encoding='utf8') as file:
    pessoas = json.load(file)
    p1 = Pessoas(**pessoas[0])
    p2 = Pessoas(**pessoas[1])
    p3 = Pessoas(**pessoas[2])

print(f'{p1.nome} tem {p1.idade} anos')
print(f'{p2.nome} tem {p2.idade} anos')
print(f'{p3.nome} tem {p3.idade} anos')
