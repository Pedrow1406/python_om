from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name

    @property 
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, value): ...
    

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Sou inútil')

    @AbstractFoo.name.setter # Faz isso porque name não foi definido nessa classe 
    def name(self, value):
        self._name = value



foo = Foo('Bar')
print(foo.name)