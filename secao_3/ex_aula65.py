# Crie uma equação com 2 numeros e um operador em string e obtenha o resultado
resp = ''
while True:
    num1 = input("Digite o 1º número: ")
    num2 = input("Digite o 2º número: ")
    if num1.isdigit() and num2.isdigit():
        operador = input("Digite o operador artimético que voce quer usar: ")
        if len(operador) > 1:
            print('Digite apenas 1 operador!')
            continue
        if operador not in '+-*/':
            print('Digite 1 operador artimético correto!')
            continue
        if len(operador) == 0:
            print('Digite algum operador!')
            continue
        else:
            equacao = f'{num1}{operador}{num2}'
            resultado = float(eval(equacao))
            print(f'O resultado da sua equação foi {resultado}')
    else:
        print("Digite um número inteiro!!")
        continue
    resp = input('Quer Continuar [S/N]: ').strip().upper()
    if 'N' in resp:
        break
