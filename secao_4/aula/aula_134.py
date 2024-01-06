def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y


def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
soma_anonima = lambda x,y: x+y

print(
    (lambda x,y:x+y)(5, 8), 
    executa(lambda x,y:x+y, 5, 8),
    executa(soma, 5, 8),
    soma(5,8)
)

duplicador = criar_multiplicador(2) #a função criar_multiplicador retorna uma definição de função ou seja a variavel duplicador vira a função multiplica, não é atoa que voce precisa colocar duplicador(e o valor) que é a msm coisa que multiplica(e o valor)
print(duplicador)
duplica = executa(
    lambda m: lambda n: m*n, 2
)
print(duplica(30))
print(duplicador(30))

print((lambda *args: sum(args))(13,7, 5, 3, 2, 19))