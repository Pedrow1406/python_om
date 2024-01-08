# Variáveis livres + nonlocal

def fora():
    a = 1 # Variável Livre
    def dentro_de_fora():
        return a
    return dentro_de_fora

dentro = fora()
print(dentro())

def concatenar(string):
    valor_final = string # Não é possivel alterar variaveis livres. (Use o nonlocal para isso)
    def concatena(outra_string=''):
        nonlocal valor_final
        valor_final += outra_string
        return valor_final
    return concatena

concatena_pedrow = concatenar('Pedrow')
print(concatena_pedrow(' Melo'))
