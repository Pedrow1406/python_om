# Exercicios  com funções
"""
Crie uma função que multiplica todos os argumentos 
não nomeado recebidos.
Retorne o total para uma variável e mostre o valor da variavel
"""
def multiplica(*args):
    tot_mult = 1
    for each_args in args:
        tot_mult *= each_args
    return tot_mult

numeros = (1,2,3,4,5,6,7,8,9, 10)
print(f'O valor total da multiplicação entre {numeros} é igual a {multiplica(*numeros)}')

"""
Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
""" 

def par_impar(number):
    if number % 2 == 0:
        return 'PAR'
    return 'IMPAR'

num = input('Digite um número para saber se é par ou ímpar: ')
if num.isdigit():
    num = int(num)
    print(f'O número {num} é {par_impar(num)}')
else:
    print('Digite um número inteiro!')

