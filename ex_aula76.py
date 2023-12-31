"""
Faça um jogo para o usuário adivinha qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digita apenas uma letra
- Quando o usuário digitar uma letra, você vai conferir se a letra digita está na palavra secreta
    - Se a letra digita estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

secret_word = input('Digite a Palavra Secreta: ').upper() #Input para o Usuario da Definir a Palavra Secreta
cripto_word_list = [] #Lista para criptografar a secret_word
for percorrer in secret_word:# Para cada letra da palavra secreta
    cripto_word_list.append('*') #Adicone um '*' para os * se adaptarem ao tamanho da palavra secreta
trys_list = [] #Lista de Tentativas
trys_erro = 0 # Quantidade de Tentativas Erradas
correct_word = 0 # Quantidade de Acertos
while True:
    trys_list = [] #Lista de Tentativas Resetada apos cada intereção do loop
    letra = input('Digite uma letra e tente acertar a palavra secreta: ').upper()

    if len(letra) > 1: #Se o usuario digitar mais de uma letra.
        print('Digite apenas 1 letra por vez!')
        continue
    if len(letra) == 0: #Se o usuario não digitar nada.
        print("Digite alguma letra!")
        continue
    for indice, c in enumerate(secret_word): #Vai percorrer a string secret_word
        trys_list.append(c) #Vai adicionar cada letra da palavra secret a lista de tentativa
        if c == letra: #Se a letra da palavra secreta for igual a letra que o usuario digitou
            correct_word += 1 #A varivel correct_word recebe mais 1 a cada letra correta
            cripto_word_list[indice] = c # E se a letra for correta o item lista criptografada vira a letra
            trys_list.remove(c) #Se a letra for correta ele remove a letra correta da lista de tentativa
            for cd_cripto in cripto_word_list: #Para cada * da lista criptografada
                print(cd_cripto, end=' ') #Ele vai printar a letra e tirar a quebra de linha
            print() #print vazio para quebrar de linha para nao interferir nos outros prints
        elif c != letra: #Se a cada letra da lista da secret_word for diferente da letra que o usario digitou
            if len(trys_list) == len(secret_word): # E se a quantidade de itens da trys_list for igual a quantidade de itens da secret_word
                trys_erro += 1 #Try vai receber mais 1 ou seja soma 1 tentativa a cada erro
                print(f'Letra Incorreta. Tentativa ({trys_erro}x)') #printa que a letra esta incorreta e mostra a quant de trys

    if correct_word == len(secret_word): #Se a quantidade de letras acertadas for igual a quantidade de letras da palavra secreta
        print(f'Parabéns!!! Você Descobriu a Palavra Secreta com {trys_erro} tentativas.') #Vai printar um Parabens com a quantidade de Trys
        break # E depois vai se encerrar o loop while e vai terminar o programa.