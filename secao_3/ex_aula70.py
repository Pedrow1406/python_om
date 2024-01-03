# Mostre qual letra da frase abaixo se repetiu mais vezes
frase = 'O Python é uma linguaguem de programação  multiparadigma  Python foi criado por Guido van Rossum.'.lower().strip()  
frase_sep = frase.split()
frase_junta = ''.join(frase_sep)
i=0
max_letra = ''
max_rep = 0

while i < len(frase_junta):
    totrep = frase_junta.count(frase_junta[i])

    if max_rep < totrep:
        max_rep = totrep
        max_letra = frase_junta[i]
    i += 1
print(f'a letra que mais se repetiu foi a letra "{max_letra}" e ela se repetiu {max_rep} vezes')
