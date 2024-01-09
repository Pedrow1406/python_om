"""
Funções decoradoras e decoradores
Decorar = Adiconar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções
"""
def criar_funcao(func):

    def interno(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    
    return interno
def inverte_string(string):
    return string[::-1]

def is_string(param):
   if not isinstance(param, str):
       raise TypeError('Parametro deve ser uma string')
inverte_string_check_parametro =  criar_funcao(inverte_string)

invertida = inverte_string('PEDRO')
print(invertida)