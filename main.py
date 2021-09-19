import random

def status(lives):
    if(lives == 9):
        print("9 lives left")
        print("  --------  ")
    if(lives == 8):
        print("8 lives left")
        print("  --------  ")
        print("     O      ")        
    if(lives == 7):
        print("7 lives left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
    if(lives == 6):
        print("6 lives left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    /       ")
    if(lives == 5):
        print("5 lives left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    / \     ")
    if(lives == 4):
        print("4 lives left")
        print("  --------  ")
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
    if (lives == 3):
        print("3 lives left")
        print("  --------  ")
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
    if (lives == 2):
        print("2 lives left")
        print("  --------  ")
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
    if(lives == 1):
        print("1 lives left")
        print("  --------  ")
        print("   \ O |/   ")
        print("     |      ")
        print("    / \     ")
    if(lives == 0):
        print("You loose. Your man is dead.")
        print("  --------  ")
        print("   \ O_|   ")
        print("     |      ")
        print("    / \     ")



def hangman():
    word = random.choice(["motorbyke", "house", "elevator", "president", "tyranosaurus", "helicopter"])
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lives = 10
    guessmade = ''

    while(len(word) > 0):
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in letters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character: ")
            guess = input()
        if guess not in word:
            lives = lives - 1
            status(lives)
            if(lives == 0):
                break
        

print("Welcome to the game! Try to guess a word in less than 10 attempts.")
hangman()