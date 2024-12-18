import random

while True:
    print("Welcome to Number Guessing Game")
    print("You have to guess a number between 1 to 100")
    print("Select the levels of difficulty")
    print("1.Easy\n2.Medium\n3.Hard")
    choice = int(input("Select Level: "))
    attempts = 3
    if choice == 1:
        print("YOU SELECTED EASY LEVEL")
        print("You have to guess a number between 1 to 30")
        guessnum = random.randint(1, 30)
        for i in range(3):
            cho = int(input("Enter your guess: "))
            if cho == guessnum:
                print("YOU WON")
                break
            elif cho > guessnum:
                print("YOU ENTERED A HIGHER NUMBER") 
                attempts = attempts - 1
                print("You have", attempts, "chances left")
            elif cho < guessnum:
                print("YOU ENTERED A LOWER NUMBER")
                attempts = attempts - 1
                print("You have", attempts, "chances left")
            elif attempts == 0:
                print("YOU LOSE")
                break

    elif choice == 2:
        print("YOU SELECTED MEDIUM LEVEL")
        print("You have to guess a number between 1 to 20")
        guessnum = random.randint(1, 50)
        for i in range(3):
                cho = int(input("Enter your guess: "))
                if cho == guessnum:
                    print("YOU WON")
                    break
                elif cho > guessnum:
                    print("YOU ENTERED A HIGHER NUMBER")
                    attempts -= 1
                    print("You have", attempts, "chances left")
                elif cho < guessnum:
                    print("YOU ENTERED A LOWER NUMBER")
                    attempts -= 1
                    print("You have", attempts, "chances left")
                elif attempts == 0:
                    print("YOU LOSE")
                    break

    elif choice == 3:
        print("YOU SELECTED HARD LEVEL")
        print("You have to guess a number between 1 to 100")
        guessnum = random.randint(1, 100)
        for i in range(3):
                cho = int(input("Enter your guess: "))
                if cho == guessnum:
                    print("YOU WON")
                    break
                elif cho > guessnum:
                    print("YOU ENTERED A HIGHER NUMBER") 
                    attempts -= 1
                    print("You have", attempts, "chances left")
                elif cho < guessnum:
                    print("YOU ENTERED A LOWER NUMBER")
                    attempts -= 1             
                    print("You have", attempts, "chances left")
                elif attempts == 0:
                    print("YOU LOSE")
                    break
                
                
    elif choice > 3:
        print("Invalid input")
        break

    play = input("Do you want to play again? (yes/no): ")
    if play == "no":
        break
    elif play == "yes":
        continue
    else:
        print("Invalid input")
        break