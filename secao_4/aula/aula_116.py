"""
Clousure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar
        

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite= criar_saudacao('Boa noite')

print(falar_bomdia('Pedrow'))
print(falar_boanoite('Pedrow'))
print('=-'*20)
for cada_nome in ['Pedro', 'Joao', 'Maria']:
    print(falar_bomdia(cada_nome))
    print(falar_boanoite(cada_nome))
print('=-'*20)