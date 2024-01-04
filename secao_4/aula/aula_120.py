# Manipulando chaves e valores em dicionários

pessoa = {}


pessoa['nome'] = 'Pedrow'
pessoa['idade'] = 18
print(f'{pessoa['nome']} tem {pessoa['idade']} anos.')
pessoa['sobrenome'] = 'Melo'
del pessoa['sobrenome']
# print(pessoa['sobrenome']) == Vai da erro porque essa key foi deletada
if pessoa.get('sobrenome') is None: #Retorna None se essa key não existir
    print('Essa chave não existee')
else:
    print(pessoa['sobrenome'])