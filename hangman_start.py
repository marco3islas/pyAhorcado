import random
from art import stages, logo
from palabras import word_list
import os
def clear(): os.system('clear')


# Step 1


# random_word = random.randint(0, len(word_list) - 1)

display = []
espacio = "_"
lives = 6
print(logo)
choosen_word = random.choice(word_list)
choosen_word = choosen_word.lower()
# choosen_word = list(choosen_word)
word = len(choosen_word)
for letter in range(word):
    display += espacio

end_of_game = False

while not end_of_game:
    guess= input("Adivina una letra de la palabra escondida: ").lower()

    clear()

    if guess in display:
        print(f"Esa letra ya la adivinaste antes. {guess}")

    for position in range(word):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in choosen_word:
        lives -= 1
        print(f"La letra {guess} no esta en esta palabra. Pierdes una vida.")
        if lives == 0:
            end_of_game = True
            print(f"You Lose, la palabra es: {choosen_word}")
    print(f"Este es el numero de letras de la palabra escondida: \n{' '.join(display)}")
    if espacio not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
