"""
Sets - Conjuntos em Pythons (tipo set)
Conjuntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipo imutáveis como valor interno


Criando um set
set(iterável) ou {1,2,3}
"""
s1 = {'Pedrow',1,2,3} # Não garante ordem
print(s1,type(s1))
s1 = set('Pedrow') # Não garante ordem
print(s1,type(s1))

"""
Sets são eficientes para remover valores duplicados de iteráveis

*Eles não tem index(indice)
*Eles não garantem ordem
*Eles são iteráveis (for, in, not in)
"""
s1 = {1,2, 3, 5, 5, 5, 4, 5, 3, 2, 1,} # Descarta os valores duplicados
print(s1)
for cada_item in s1:
    print(cada_item, end = ' ') # Sets são Iteráveis
print()
"""
Métodos Úteis:
add, update, clear, discard
"""
s1.add(6) # Adiciona um item no set
print(s1)
s1.discard(5) #Descarta 1 valor do set
print(s1)
s1.clear() #Limpa o set (elemina todos os valores do set)
print(s1)

"""
Operadores úteis:
união | união(union) - Une
itersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 #Une os 2 sets
print(s3)
s3 = s1 & s2
print(s3) # Exibe apenas os itens presentes nos 2 sets
s3 = s1 - s2  
print(s3)# Itens APENAS presentes no set da esquerda que não tem no set da direito que no caso é o s1
s3 = s1 ^ s2 
print(s3) # Oposto a Intersecção. Exibe apenas os itens NÃO presentes nos 2 sets

