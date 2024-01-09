"""
Exercício - Unir listas 
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem
Use todos os valores da menor lista
Ex.:
['Salvador','Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA')('Ubatuba','SP')('Belo Horizonte', 'MG')]
"""

def zipper(city, abr):
    listas_unidas = []
    if len(city) < len(abr):
        for contador in range(len(city)):
            listas_unidas.append((city[contador], abr[contador]))
        return listas_unidas
    for contador in range(len(abr)):
        listas_unidas.append((city[contador], abr[contador]))
    return listas_unidas

cidades = ['Salvador','Ubatuba', 'Belo Horizonte']
abreviacao = ['BA', 'SP', 'MG', 'RJ']
zipado = zipper(cidades, abreviacao)
print(*zipado, sep = '\n')