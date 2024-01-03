"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista
"""
import os
compras = []
def mostra_lista():
    for cada_produto in range(len(compras)):
        print(f'{cada_produto} {compras[cada_produto]}')
while True:
    produto = input('Qual produto você quer comprar: ').strip().capitalize()
    compras.append(produto)
    continua = input('Voce quer continuar comprando [S/N]: ').strip().upper()
    resp = ''
    loops = False
    if continua not in 'SN':
        print('Digite apenas [S] ou [N]')
        continue
    elif continua in 'SN':
        if 'S' in continua:
            continue
        else:
            while True:
                os.system('cls')
                if len(compras) == 0:
                    loops = False
                    print('Sua lista de compras esta vazia no momento.')
                    resp = input('Voce deseja comprar algum produto [S/N]: ').strip().upper()
                    if resp not in 'SN':
                        print('Digite apenas [S] ou [N]')
                        continue
                    elif resp in 'SN':
                        break
                else:
                    print('Sua lista de compras atual é: ')
                    mostra_lista()
                if loops: #So vai entrar no loop se o loop for True. Condicional criada pq no momento não existe essas variáveis.
                    if 'S' in deletar:
                        produto_deletar = input('Qual produto voce deseja deletar?(Digite o Numero do Produto): ').strip()
                        if produto_deletar.isdigit():
                            produto_deletar = int(produto_deletar)
                            if produto_deletar >= len(compras):
                                print('Não existe um produto com esse numero.')
                            else:
                                compras.pop(produto_deletar)
                                os.system('cls')
                                mostra_lista()
                        else:
                            print('Porfavor digite o Numero do Produto.')
                if len(compras) > 0:
                    deletar = input('Deseja deletar algum item da sua lista [S/N]: ').strip().upper()
                else:
                    continue
                if deletar not in 'SN':
                    print('Digite apenas [S] ou [N]')
                else:
                    if 'S' in deletar:
                        loops = True
                        continue
                    if 'N' in deletar:
                        loops = False
                        break
                if 'S' in resp or 'N' in resp:
                    break
    if len(compras) > 0:
        resp = input('Voce deseja comprar mais algum produto [S/N]: ').strip().upper()
        if resp not in 'SN':
            print('Digite apenas [S] ou [N]')
            continue
        elif resp in 'SN':
            if 'S' in resp:
                continue

    if 'N' in deletar or 'N' in resp:
        os.system('cls')
        print('Compra Encerrada!')
        if len(compras) == 0:
            print('Infelizmente você decidiu não comprar nada.')
            break
        print('Sua lista de compras foi: ')
        mostra_lista()
        break
print('Tenha um Bom Dia!')