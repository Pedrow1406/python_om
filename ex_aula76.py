"""
Faça um jogo para o usuário adivinha qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digita apenas uma letra
- Quando o usuário digitar uma letra, você vai conferir se a letra digita está na palavra secreta
    - Se a letra digita estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

secret_word = input('Digite a Palavra Secreta: ').upper() #Input para o Usuario da Definir a Palavra Secreta
secret_letters = ["*" for each_letter in range(len(secret_word))] #Lista para criptografar a secret_word

fail_count = 0 # Quantidade de Tentativas Erradas
correct_len = 0 # Quantidade de Letras corretas
while True:
    letter = input('Digite uma letra e tente acertar a palavra secreta: ').upper()

    if len(letter) > 1: #Se o usuario digitar mais de uma letra.
        print('Digite apenas 1 letra por vez!')
        continue
    if len(letter) == 0: #Se o usuario não digitar nada.
        print("Digite alguma letra!")
        continue

    #Realiza uma busca pela letra na palavra
    found = False 
    for i, c in enumerate(secret_word): #Vai percorrer a string secret_word
        if c == letter: #Se a letra da palavra secreta for igual a letra que o usuario digitou
            correct_len += 1 #A varivel correct_len recebe mais 1 a cada letra correta
            secret_letters[i] = c # E se a letra for correta o item lista criptografada vira a letra
            found = True 
    
    #Verifica o resultado da busca
    if found:
        for cd_cripto in secret_letters: #Para cada * da lista criptografada
                    print(cd_cripto, end=' ') #Ele vai printar a letra e tirar a quebra de linha
        print() #adiciona quebra de linha
    else:
        fail_count += 1 #Try vai receber mais 1 ou seja soma 1 tentativa a cada erro
        print(f'Letra Incorreta. Contagem de erros em ({fail_count}x)') #printa que a letra esta incorreta e mostra a quant de trys
        
    if correct_len == len(secret_word): #Se a quantidade de letras acertadas for igual a quantidade de letras da palavra secreta
        print(f'Parabéns!!! Você Descobriu a Palavra Secreta com {fail_count} tentativas falhas.') #Vai printar um Parabens com a quantidade de Trys
        break # E depois vai se encerrar o loop while e vai terminar o programa.