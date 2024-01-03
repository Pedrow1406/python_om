"""
Higher Order Funcitions
Funções de primeira classe
"""


def saudacao(msg, nome='Pedrow'):
    return f'{msg}, {nome}!'

def executa(funcao,*args):
    if 1<= len(args) <= 2:
        return funcao(*args)
    return f'Digite apenas a função, mensagem e o nome da pessoa'

print(
    executa(saudacao, 'Bom dia')
)
print(
    executa(saudacao, 'Bom dia', 'Luiz')
)