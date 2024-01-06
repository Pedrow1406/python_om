"""
Função lambda em Python
A função lamda é uma função como qualquer outra em Python. Porém, são funções anónimas
que contém apenas uma linha. Ou seja, tudo 
deve ser contidio dentro de uma única expressão. 
lista = [
    {'nome': 'Pedrow' , 'sobrenome': 'Melo'}
    {'nome': 'Massiele' , 'sobrenome': 'Porto'}
    {'nome': 'Julio' , 'sobrenome': 'Cesar}
    {'nome': 'Otávio' , 'sobrenome': 'Miranda'}
    {'nome': 'Lucas' , 'sobrenome': 'Montana'}
]
"""
lista = [3, 5 , 7, 8, 9, 10, 2, 1, 6, 4,]
lista.sort(reverse=True)
print(lista)

lista = [
    {'nome': 'Pedrow' , 'sobrenome': 'Melo'},
    {'nome': 'Bruno' , 'sobrenome': 'Sousa'},
    {'nome': 'Massiele' , 'sobrenome': 'Porto'},
    {'nome': 'Julio' , 'sobrenome': 'Cesar'},
    {'nome': 'Otávio' , 'sobrenome': 'Miranda'},
    {'nome': 'Lucas' , 'sobrenome': 'Montana'}
]
def exibir(lista):
    for each_item in lista:
        print(each_item)

def linha():
    print('-='*25)
#Ordenando com a função normal usando o metodo .sort()
# def orderna(item):
#     return item['nome']
# lista.sort(key=orderna)
# exibir(lista)

#Ordernando com a função lambda usando o metodo .sort()
lista.sort(key=lambda item:item['nome'])
exibir(lista)
linha()
#Ordenando com a função lambda usar a função sorted()
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['nome'], reverse=True)

exibir(l1)
linha()
exibir(l2)
linha()