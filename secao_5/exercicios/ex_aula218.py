"""
Exercícios com classes
1 - Crie uma classe Carro (Nome)
2 - Crie uma classe Motor (Nome)
3 - Crie uma classe Fabricante (Nome)
4 - Faça a ligação entre Carro e Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricante na tela
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._fabricante = None
        self._motor = None
    
    @property
    def motor(self):
        return self._motor 
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        return self._fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
fusca.fabricante = Fabricante('Volkswagen')
fusca.motor = Motor('1.0')

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
