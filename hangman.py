import random
from words import word_file


def the_word():
    word = random.choice(word_file)
    return word.upper()


def display(word):
    whole_word = "_" * len(word)
    guessed = False
    guess_letter = []
    guss_word = []
    attempts = 8
    print("Let's play Hangman!")
    print(display_hangman(attempts))
    print(whole_word)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guess_letter:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guess_letter.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guess_letter.append(guess)
                word_as_list = list(whole_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                whole_word = "".join(word_as_list)
                if "_" not in whole_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guss_word:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guss_word.append(guess)
            else:
                guessed = True
                whole_word = word
        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(whole_word)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of attempts.\nYou killed a pure soul :( The word was " + word + "\nMaybe next time!")


def display_hangman(attempts):
    levels = [  
                """
                   --------
                   |      | /
                   |      O/
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        
                """
                   --------
                   |      |
                   |      O/
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return levels[attempts]


def main():
    word = the_word()
    display(word)
    while input("display Again? (Y/N) ").upper() == "Y":
        word = the_word()
        display(word)


if __name__ == "__main__":
    main()