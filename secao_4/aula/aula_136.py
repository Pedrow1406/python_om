"""
List comprehension em Python
List comprehesion é uma forma rápida para criar listas
a partri de iteráveis
"""

string = 'Pedrow'
cripto_string = ['*' for each_letter in string]
print(cripto_string)

numeros = [1, 6, 3, 2, 1, 6, 2, 6, 7, 1]
triplo_numeros = [cada_numero * 3 for cada_numero in numeros]
print(triplo_numeros)

lista = [ contagem ** 2  for contagem in range(1,11) if contagem % 2 == 0]
print(lista)


# Mapeamento de dados em list comprehesion
produto = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 20}
]
novo_produto = [{**each_produto, 'preco':each_produto['preco'] * 1.2} if each_produto['preco'] > 20 else each_produto for each_produto in produto if each_produto['preco'] >= 20]
print(*produto)
print(novo_produto)
