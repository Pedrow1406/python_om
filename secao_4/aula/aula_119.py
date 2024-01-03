pessoa = {
    'nome': 'Pedrow',
    'sobrenome': 'Melo',
    'idade': 18,
    'altura': 1.65,
    'endereco': [
        {'rua': 'João Pessoa', 'numero': 2411},
        {'rua': 'Marechal', 'numero': 520},
    ],
}

print(f'{pessoa['nome']} tem {pessoa['idade']} anos.')

for each_atributte in pessoa:
    print(f'{each_atributte} = {pessoa[each_atributte]}')
