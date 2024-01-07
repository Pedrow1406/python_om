"""
Exercícios
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
"""
def exibir(lista):
    for novo_produto in lista:
        print(novo_produto)
    print()
from copy import deepcopy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 31.42},
    {'nome': 'Produto 4', 'preco': 42.81},
    {'nome': 'Produto 3', 'preco': 8.99},
    {'nome': 'Produto 1', 'preco': 153.80}
]

novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1, 2)}for produto in deepcopy(produtos)]
exibir(novos_produtos)
"""
Ordene os produtos por nome descrescente (do maior para menor)
gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""
produtos_ordenados_por_nome = sorted(deepcopy(novos_produtos), key= lambda p :p['nome'],reverse=True)
exibir(produtos_ordenados_por_nome)
"""
Ordene os produtos por preco crescente (do menor para maior)
gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
produtos_ordenados_por_preco = sorted(deepcopy(novos_produtos), key= lambda p :p ['preco'])
exibir(produtos_ordenados_por_preco)