# Exercícios
"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""

# Feito por Pedrow1406

# def duplica(number):
#     return number * 2

# def triplica(number):
#     return number * 3

# def quadruplica(number):
#     return number * 4

# num = input('Digite um Numero Inteiro: ')
# if num.isdigit():
#     num = int(num)
#     duplicado = duplica(num)
#     triplicado = triplica(num)
#     quadruplicado = quadruplica(num)
#     print(f'Número Duplicado: {duplicado}')
#     print(f'Número Triplicado: {triplicado}')
#     print(f'Número Quadruplicado: {quadruplicado}')
# else:
#     print('Digite um número Inteiro')

# Feito por Otávio Miranda
# Usando Função para criar outras funções

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


num = input('Digite um Numero Inteiro: ')
if num.isdigit():
    num = int(num)
    duplicar = criar_multiplicador(2)
    triplicar = criar_multiplicador(3)
    quadruplicar = criar_multiplicador(4)
    centuplicar = criar_multiplicador(100)
    print(f'Número Duplicado: {duplicar(num)}')
    print(f'Número Triplicado: {triplicar(num)}')
    print(f'Número Quadruplicado: {quadruplicar(num)}')
    print(f'Número Centuplicado: {centuplicar(num)}')
else:
    print('Digite um número Inteiro')