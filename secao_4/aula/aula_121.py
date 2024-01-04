"""
Méetodos úteis dos dicionários em Python
len = quantas chaves
keys = iterável com as chaves
values = iterável com os valores
items = iterável com chaves e valores
setdefault = adiciona valor se a chave não existir
copy = retorna uma cópia rasa (shallow copy)(copia apenas valores imutuveis e linka os mutáveis)
get = obtém uma chave
pop = Apaga o ultimo item com a chave especificada (del)
popitem = Apaga o ultimo item adicionado
update = Atualiza um dicionário com outro
"""
pessoa = {
    'nome': 'Pedrow',
    'sobrenome': 'Melo',
}

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
print(pessoa.setdefault('idade', 18))

print('-='*25)

for chave, valor in pessoa.items():
    print(f'{chave} é {valor}')
