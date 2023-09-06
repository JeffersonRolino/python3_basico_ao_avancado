"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

running = True
game_over = False

secret_word = "love"
choosen_letters = []
chances = 5
attempts = 0
hits = 0
message = ""

while running:
    os.system("clear")
    print("-" * 52)
    print(f"LETROCA\t\tChances: {chances}\t\tAttempts: {attempts}")
    print("-" * 52)
    print(f"Your secret word has {len(secret_word)} letters: ")

    word = ""
    for char in secret_word:
        if char in choosen_letters:
            word += char
        else:
            word += "*"
    print(f"\nSecret Word: {word}")

    print(f"\n{message}\n")

    if not game_over:
        running = True

    if game_over:
        running = False

    while not game_over:
        letter = input("Please choose a word: ")

        is_digit = letter.isdigit()
        only_one_letter = len(letter) == 1

        if is_digit:
            message = "\tSorry, numbers are not valid..."
            break
        elif not only_one_letter:
            message = "\tSorry, you must type only one letter..."
            break
        else:
            attempts += 1
            choosen_letters.append(letter)
            if letter in secret_word:
                hits += 1
                if hits < len(secret_word):
                    message = f"\tYou hit! The letter '{letter}' is in the secret word"
                    break
                else:
                    message = "\tCONGRATULATIONS! YOU WON!"
                    game_over = True
                    break
            else:
                chances -= 1
                if chances > 0:
                    message = (
                        f"\tYou miss! The letter '{letter}' is not in the secret word"
                    )
                    break
                else:
                    message = f"\tYOU LOST!\n\tThe secret word was: {secret_word}"
                    game_over = True
                    break
