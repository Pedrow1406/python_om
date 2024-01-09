"""
Considerando duas listas de inteiros ou floats (lita A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.
 
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

Resultado
lista_soma = [2, 4, 6, 8]
"""

def soma_listas(l1, l2):
    menor_lista = min(len(l1), len(l2))
    lista_soma = [l1[c] + l2[c] for c in range(menor_lista)]
    return lista_soma

lista_a = [1, 2.4, 3, 4, 5, 6, 7]
lista_b = [1, 2.6, 3, 4, 11.2]
lista_somada = soma_listas(lista_a, lista_b)
print(lista_somada)