"""
  Herança
Uma classe pode herdar atributos e métodos de outra classe
"""
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome  = sobrenome
        self._nome_class = None
    
    @property
    def falar_nome_class(self):
        self._nome_class = self.__class__.__name__
        return self._nome_class
    
class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...
c1 = Cliente('Pedrow', 'Melo')
c2 = Aluno('João', 'Vitor')
print(f'{c2.nome} {c2.sobrenome} é {c2.falar_nome_class}')
print(f'{c1.nome} {c1.sobrenome} é {c1.falar_nome_class}')
help(Cliente())