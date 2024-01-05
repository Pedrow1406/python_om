"""
Exercício 
Criee uma função que encontre o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisistos:
    A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número duplicado em si. 
    Exemplo:
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1  (Não tem duplicados)
        [1, 4, 9, 8, -> 9 <-, 4, 8] Retorne 9
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 4, 8, 6, 5, 9, 6, 7],
    [4, 8, 8, 8, 5, 10, 6, 7 , 5, 2],
    [3,2, 3, 2, 5, 6, 5, 6, 7, 8, 7],
    [10, 9, 8 , 7, 6, 5, 4, 3, 2 ,1],
    [1, 4, 9, 8, 9,  4, 8]
]
def itens_duplicados(lista):
    numeros = []
    duplicados = set()
    for cada_item in lista:
        if cada_item not in numeros:
            numeros.append(cada_item)
        elif cada_item in numeros:
            duplicados.add(cada_item)
    duplicados = list(duplicados)
    if len(duplicados) > 1:
        print(f'O {duplicados[1]} foi a segunda ocorrência dos valores duplicados')
    if not duplicados:
        return -1
    return len(duplicados)

def linha():
    print('-=' * 25)

for cada_lista in lista_de_listas_de_inteiros:
    linha()
    duplicado = itens_duplicados(cada_lista)
    if duplicado == -1:
        print(f'A lista {cada_lista} não repetiu nenhum valor')
    else:
        print(f'A lista {cada_lista} repetiu {duplicado} valor(es)')