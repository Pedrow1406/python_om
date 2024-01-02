"""
CALCULO DO SEGUNDO DIGITO DO CPF
CPF: 756.834.809-70
Colete a a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicado cada um dos valores por uma 
contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)
    11 10  9  8  7  6  5  4  3 2
    7  4   6  8  2  4  8  9  0 7
   77  40  54 64 14 24 40 36 0 14

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 381
Multiplicar o resultado anterior por 10
381 * 10 = 3810
Obter o resto da divisão da conta anterior por 11
3810 % 11 = 7
Se o resultado anterios for maior que 9:
    resultado é 0
cantrário disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
"""
cpf = []
contagem_regressiva = 11
soma = 0
while True:
    cpf_numero = input('Digite seu CPF: ')
    list_cpf_numero = list(cpf_numero)
    if '-' in cpf_numero or '.' in cpf_numero:
        for _ in list_cpf_numero:
            if _ == '-' or _ == '.':
                list_cpf_numero.remove(_)
        cpf_numero = ''.join(list_cpf_numero)
    if 10<=len(cpf_numero)<=11:
        if cpf_numero.isdigit():
            for adiciona_cpf in cpf_numero:
                adiciona_cpf = int(adiciona_cpf)
                if len(cpf) < 10:
                    cpf.append(adiciona_cpf)
            print(f'Os 9 primeiros digitos do seu CPF são {cpf}')
            break
        else:
            print('Digite o cpf apenas com numeros inteiros!!')
            continue
    else:
        print('Seu CPF tem que conter 10 ou 11 digitos')
        continue
for digito in cpf:
    resultado = digito * contagem_regressiva
    soma += resultado
    contagem_regressiva -= 1
multi_10 = soma * 10
segundo_digito = multi_10 % 11 
segundo_digito = segundo_digito if 0 <= segundo_digito <= 9 else 0
print(f'O segundo digito do seu CPF é {segundo_digito}')