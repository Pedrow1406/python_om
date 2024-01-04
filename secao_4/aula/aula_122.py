# Shallow Copy vs Deep Copy
# Shallow copy = copy() = copia apenas os valores imutaveis do dicionarios. Faz uma copia rasa 
# Deep Copy = import copy 
                #copy.deepcopy()
#Copia tudo incluindo os valores mutáveis. Faz uma copia profunda

import copy 

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}
d2 = d1.copy() # Shallow Copy

d2['c1'] = 1000
d2['l1'][1] = 500 # Shallow Copy não copia valores mutaveis

print(d1)
print(d2)

print('=-' * 20)

d2 = copy.deepcopy(d1) # Deep Copy

d2['c1'] = 1000
d2['l1'][1] = 376 # Deep Copy COPIA valore mutáveis
print(d1)
print(d2)
