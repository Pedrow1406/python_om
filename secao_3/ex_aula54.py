"""
Faça um programa que peça ao usuário para digitar um numero inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteirio, informe que não é um núemro inteirio.
"""
numero = input('Digite um número: ')
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    elif numero % 2 != 0:
        print(f'O número {numero} é impar')
else:
    print('O valor digitado não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
# """
horas = input('Digite a hora atual: ')
if horas.isdigit():
    horas = int(horas)
    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 12 <= horas <= 17:
        print('Boa Tarde!')
    elif 18 <= horas <= 23:
        print('Boa Noite!')
else:
    print('Digite um horário válido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande" 
"""

while True:
    nome = input('Informe seu primeiro nome: ')
    if nome:
        if len(nome) <= 2:
            print('Nome Invalido!')
            continue
        elif len(nome) <= 4:
            print('Seu nome é curto')
        elif 5<= len(nome) <= 6:
            print('Seu nome é normal')
        elif len(nome) > 6:
            print('Seu nome é muito longo')
        break
    else:
        print('Nada foi Digitado!')