import json 
import os
caminho_pasta_pai = os.path.dirname(__file__) # C:\Users\apfri\Pictures\Desktop\pedro_pasta\PEDRO PROGRAMAÇÃO\python_om\secao_4\aula
caminho_nome = os.path.join(caminho_pasta_pai, 'exemplo2.json') # C:\Users\apfri\Pictures\Desktop\pedro_pasta\PEDRO PROGRAMAÇÃO\python_om\secao_4\aula\exemplo2.json
burrice = [
    {"nome": "Pedrow", "idade": 18, "sexo": "Masculino"},
    {"nome": "Maria", "idade": 15, "sexo": "Feminino"},
    {"nome": "Felipe", "idade": 13, "sexo": "Masculino"},
    {"nome": "João", "idade": 25, "sexo": "Masculino"}
]
with open(caminho_nome, 'w', encoding='utf8') as file:
    json.dump(burrice, file, indent=2, ensure_ascii=False) #No json.dump(tem que passar como parametro o iterável e dps o arquivo)

with open(caminho_nome, 'r', encoding='utf8') as arquivo:
    sla = json.load(arquivo) # Retorna o arquivo json
    print(*sla, sep='\n')

# os.remove('C:\\Users\\apfri\Pictures\Desktop\pedro_pasta\PEDRO PROGRAMAÇÃO\python_om\secao_4\\aula\exemplo2')