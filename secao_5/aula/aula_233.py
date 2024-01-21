"""
- Criando Exceptions em Python Orientado a Objetos
- Para criar uma Exception em Python, você só precisa herdar de alguma
exceção da linguagem.
- A recomendação da doc é herdar de Exception
https://docs.python.org/3/library/exceptions.html
- Criando exceções (comum colocar Error ao final)
- Levantando (raise) / Lançando (throw) exceções
- Relançando exceções
- Adicionando notas em exceções (3.11.0)
"""

class MeuError(Exception):
    ...
class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1') 
    raise exception_

try: # Tratando meu error
    levantar()
    1/0
except( MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Essa é a nota desse error')
    raise exception_ from error # Relançando Exceção