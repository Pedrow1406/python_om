# Adicione um * entre cada letra de uma string
nome = input('Digite seu nome: ')
cont = 0
while cont < len(nome):
    novo_nome = f'*{nome[cont]}'
    if cont == len(nome)-1:
        novo_nome = f'*{nome[cont]}*'
    cont+=1
    print(novo_nome, end='')