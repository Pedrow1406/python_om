# Exericício - Adiando execução de funções
#                   C L O S U R E
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna

soma_com_sete = criar_funcao(soma, 7)
multiplica_por_100 = criar_funcao(multiplica, 100)
print(soma_com_sete(10))
print(multiplica_por_100(4))