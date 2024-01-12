"""
Criando e Manipulando arquivos com Python 
Usamos a função open() para brir um arquivo em Python (ele pode existir ou não)

Modos:
r (leitura), w(escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto)
+ (leitura e escrita)
Context manager - with (abre e fecha)

Diferença entre w(write) e a(append):
w = apaga tudo que esta no arquivo e escreve
a = não apaga tudo que esta no arquivo e escreve
ou seja... se você quiser reescrever um arquivo use o w. Se voce quiser adicionar e não quer que seu arquivo perca os dados anteriores use o a.

Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler várias linhas)

Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - renomeia ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json, mas:
json.load
"""
import os

nome_arquivo= 'aula_186.txt'
caminho_completo_arquivo = 'C:\\Users\\apfri\\Pictures\\Desktop\\pedro_pasta\\PEDRO PROGRAMAÇÃO\\python_om\\secao_4\\aula\\aula_186.txt'

# Abrindo arquivo com open e fechando com o close
arquivo_com_open = open(nome_arquivo, 'w') # Cria um arquivo na raiz do projeto
arquivo_com_open = open(caminho_completo_arquivo,  'w') # Cria um arquivo em um local especifico
arquivo_com_open.close() # Fecha o Arquivo

# Abrindo e Fechando arquivo com o with open
with open(caminho_completo_arquivo, 'w+') as arquivo_com_with: # with abre e fecha o arquivo
    print('Arquivo ABERTO')

    arquivo_com_with.write('Linha 1\n')
    arquivo_com_with.write('Linha 2\n')
    arquivo_com_with.writelines(('Linha 3\n', 'Linha 4\n')) # Escreve algo no arquivo mas tem que passar um iteravel (lista ou tupla)
    arquivo_com_with.seek(0 , 0) # Coloca o cursor no começo do arquivo
    print(arquivo_com_with.readline()) # Ler apenas a linha de onde esta o cursor

    arquivo_com_with.seek(0,0)
    print(arquivo_com_with.read()) # ler todo o arquivo (retorna uma string). Faz uma leitura de todo o arquivo apartir do cursor (para posicionar o cursor use o seek)
    
    arquivo_com_with.seek(0, 0)
    print(arquivo_com_with.readlines()) # Ler todo o arquivo (retorna uma lista). Faz uma leitura de todo o arquivo apartir do cursor (para posicionar o cursor use o seek)
    
    arquivo_com_with.seek(0,0)
    lista = arquivo_com_with.readlines()
    for item in lista:
        print(item.strip())

    print('Arquivo FECHADO!')
print()
with open(caminho_completo_arquivo, 'a+') as arquivo_com_with:
    arquivo_com_with.write('Pedrow\n')
    arquivo_com_with.seek(0,0)
    print(arquivo_com_with.read())

# novo_caminho_completo_arquivo = 'C:\\Users\\apfri\\Pictures\\Desktop\\pedro_pasta\\PEDRO PROGRAMAÇÃO\\python_om\\secao_4\\aula\\aula_186_renomeado.txt'
# os.remove(nome_arquivo) # Deleta um arquivo 
# os.rename(caminho_completo_arquivo, novo_caminho_completo_arquivo) # Renomeia um arquivo passando o caminho antigo e o caminho novo com o nome alterado