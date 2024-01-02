#Crie Uma Função que mostre os 2 Ultimos Números do CPF
from random import randint

def cpf_completo(nove_primeiros_digitos):
    if len(nove_primeiros_digitos) == 9:
        cpf = []
        contagem_regressiva = 10
        soma = 0
        list_cpf_numero = list(nove_primeiros_digitos)
        if '-' in nove_primeiros_digitos or '.' in nove_primeiros_digitos:
            for _ in list_cpf_numero:
                if _ == '-' or _ == '.':
                    list_cpf_numero.remove(_)
            nove_primeiros_digitos = ''.join(list_cpf_numero)
        if len(nove_primeiros_digitos) == 11 or len(nove_primeiros_digitos) == 9:
            if nove_primeiros_digitos.isdigit():
                for adiciona_cpf in nove_primeiros_digitos:
                    adiciona_cpf = int(adiciona_cpf)
                    if len(cpf) < 9:
                        cpf.append(adiciona_cpf)
        for digito in cpf:
            resultado = digito * contagem_regressiva
            soma += resultado
            contagem_regressiva -= 1
        multi_10 = soma * 10
        primeiro_digito = multi_10 % 11 
        primeiro_digito = primeiro_digito if 0 <= primeiro_digito <= 9 else 0
        dez_primeiros_digitos = f'{nove_primeiros_digitos}{primeiro_digito}'


        cpf = []
        contagem_regressiva = 11
        soma = 0
        if len(dez_primeiros_digitos) == 11 or len(dez_primeiros_digitos) == 10:
            if dez_primeiros_digitos.isdigit():
                for adiciona_cpf in dez_primeiros_digitos:
                    adiciona_cpf = int(adiciona_cpf)
                    if len(cpf) < 10:
                        cpf.append(adiciona_cpf)
        for digito in cpf:
            resultado = digito * contagem_regressiva
            soma += resultado
            contagem_regressiva -= 1
        multi_10 = soma * 10
        segundo_digito = multi_10 % 11 
        segundo_digito = segundo_digito if 0 <= segundo_digito <= 9 else 0
        
        cpf = []
        nove_primeiros_digitos = list(nove_primeiros_digitos)
        for contador, digito in enumerate(nove_primeiros_digitos):
            cpf.append(digito)
            if contador == 2 or contador == 5: 
                cpf.append('.') 
        cpf = ''.join(cpf)
            
        cpf_completo = f'{cpf}-{primeiro_digito}{segundo_digito}'
        return cpf_completo
    else:
        return 'Digite apenas os 9 primeiros digitos do CPF!'

def random_cpf():
    aleatorio_lista = []
    for _ in range(0,9):
        aleatorio = randint(0,9)
        aleatorio_lista.append(str(aleatorio))
    aleatorio_lista = ''.join(aleatorio_lista)
    return cpf_completo(aleatorio_lista) 