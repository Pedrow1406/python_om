def soma(*args):
    total = 0
    for each_arg in args:
        total += each_arg
    return total 

numeros = (1,2,3,4,5,3,2,64,2,32, 82, 100, 700)
soma_total = soma(*numeros)
print(f'O resultado da soma é {sum(numeros)}')
print(f'O resultado da soma é {soma_total}')
print(sum(numeros))