# Exercício = sistema de perguntas e respostas
import os 
perguntas = 0
def alternative(correct):
    if pergunta not in 'ABCD':
        print('Digite apenas alterantivas A ou B ou C ou D')
        os.system('cls')
    else:
        global perguntas
        perguntas += 1
        if correct  in pergunta:
            global points
            points += 1
            print('Acertou : )')
        else:
            print('Errou : (')
        print()

def notas():
    one_point = 10/perguntas
    nota = one_point * points
    return nota

def linha(num=20):
    print('-='*num)


points = 0
print('Iremos fazer um 5 perguntas no final você descubrirá quantas acertou e quantas errou.')

pergunta = input('Quanto é a raiz quadrada de 16\nA)2 B)5 C)7 D)4\nEscolha a alternativa correta: ').strip().upper()
alternative('D')
pergunta = input('Qual a idade de Pedrow? \nA)13 B)15 C)18 D)24\nEscolha a alternativa correta: ').strip().upper()
alternative('C')
pergunta = input('Qual a altura de Pedrow? \nA)1.65 B)1.86 C)1.60 D)1.83\nEscolha a alternativa correta: ').strip().upper()
alternative('A')
# pergunta = input('Qual é essa linguagem de programação? \nA)Java B)Python C)Ruby D)C#\nEscolha a alternativa correta: ').strip().upper()
# alternative('B')
# pergunta = input('Quanto é 1 + 1? \nA)3 B)11 C)4 D)2\nEscolha a alternativa correta: ').strip().upper()
# alternative('D')
print()
os.system('cls')
linha(25)

print(f'Sua pontuação final foi {notas():.2f}')
if notas() < 7:
    print('MUITO BURRO!\nREPROVADOO!!!')
else:
    print('É o Ainstein em Pessoa.\nAprovado : )')
linha(25)