"""
super() é a super classe na subclsse
-- A função super() permite com que você não altere um método por completo 
se você quiser fazer alguma alteração nele mas sem sobrescreve-lo por completo 
que no caso aconteceria se você nao usasse o super()
Sintaxe:
super().nome_do_metodo()

Classe Principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (Cliente)
    -> sub clss, child class, derived class
"""
class MinhaString(str):
    def upper(self):
        print('Chamou o UPPER')
        retorno = super().upper() # Faz com que o método não seja completamente sobrescrito ou 
        return retorno
    
p1 = MinhaString('pedrow')
print(p1.upper())

class A:
    atributo_a = 'valor_a'
    def metodo(self):
        print('A')
class B(A):
    atributo_b = 'valor_b'

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor_c'
    def metodo(self):
        print('C')
a = A()
b = B()
c = C()

print(c.atributo_b)
print(b.atributo_a)
print(a.atributo_a)