def mostro_arugumentos_nomeados(**kwargs): # kwargs empacota em um dicionario com argumentos nomeados.
                                           # args empacota em uma tupla com argumentos posicionais
    for key, value in kwargs.items():
        print(f'{key} == {value}')

mostro_arugumentos_nomeados(nome='Pedrow', idade = 18, sexo = 'masculino')

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4
}

mostro_arugumentos_nomeados(**configuracoes) # Desempacota um dicionário