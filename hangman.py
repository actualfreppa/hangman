
from random import choice
from string import ascii_lowercase

NUMBER_OF_TRYS = 6

with open("words.txt", "r") as f:
    word_list = [word.strip().lower() for word in f.readlines()]



print("Welcome to HangMan")
name = input("Please enter your name: ")

game_on = True
while game_on:
    random_choice_word = choice(word_list)

    dot_list = ["_" for _ in range(len(random_choice_word))]
    tried_characters = []
    trys = 0

    print("Staring game...")

    while trys < 6:
        print(" ".join(dot_list))
        print(f'{name}, you have {NUMBER_OF_TRYS - trys} tries left. Tried characters: [{" ". join(tried_characters)}]')
        player_choice = input("Please enter a character: ").lower()
        if player_choice in tried_characters or player_choice not in ascii_lowercase or player_choice == "":
            print(f'Invalid character or you have already tried {player_choice}. Choose a new character')
            #continue
        elif player_choice not in random_choice_word:
            print(f"Sorry, {player_choice} is not correct.")
            tried_characters.append(player_choice)
            trys += 1
        else:
            print("Correct...")
            indexes = [i for i in range(len(random_choice_word)) if player_choice == random_choice_word[i]]
            for i in indexes:
                dot_list.pop(i)
                dot_list.insert(i, player_choice)  
            tried_characters.append(player_choice)
        if "".join(dot_list) == random_choice_word:
            print(f"You won! ", end="")
            break
    print(f"Correct word is: {random_choice_word}")
    ask = input("Do you want to play again? (y/n)")
    if ask.lower() == "n":
            print("Bye, bye!")
            game_on = False
            


    

