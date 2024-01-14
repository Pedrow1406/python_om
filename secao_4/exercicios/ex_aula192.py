"""
Exercício - Crie uma Lista de tarefas permitindo que o usuário possa listar, desfazer e refazer 
"""
import os 
original_lista = []
lista = []

def mostra_lista():
    for item in lista:
        print(f'- {item.capitalize()}')

while True:
    if len(lista) > 0:
        mostra_lista()
    digito = input('Comandos: [L]istar, [D]esfazer, [R]efazer, [E]ncerrar\nDigite uma tarefa ou comando: ').strip().lower()
    os.system('cls')
        
    if digito not in 'ldre':
        if digito not in original_lista:
            original_lista.append(digito)
        print(original_lista)
        if digito not in lista:
            lista.append(digito)
    else:
        print(original_lista)
        if digito in 'l':
            if len(lista) <= 0:
                print('Não há itens para serem listados.')
            else:
                os.system('cls')
                print('Lista Atual:')
        elif digito in 'd':
            if len(lista) <= 0:
                print('Não há nenhum item para ser desfeito')
            else:
                lista.pop(-1)
        elif digito in 'r':
            if len(lista) == len(original_lista):
                print('Não há nenhum item para ser refeito')
            else:
                if original_lista[len(lista)] not in lista: 
                    lista.append(original_lista[len(lista)])
                else:
                    for each_item in original_lista:
                        if each_item not in lista:
                            lista.append(each_item)
                            break
        elif digito in 'e':
            print(f'Sua lista de Tarefas foi: ')
            mostra_lista()
            print('Programa Encerrado!')
            break
        