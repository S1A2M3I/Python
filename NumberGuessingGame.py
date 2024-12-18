import random

while True:
    print("Welcome to Number Guessing Game")
    print("You have to guess a number between 1 to 100")
    print("Select the levels of difficulty")
    print("1.Easy\n2.Medium\n3.Hard")
    choice = int(input("Select Level: "))
    attempts = 3
    end = 0
    if choice == 1:
        print("YOU SELECTED EASY LEVEL")
        end = 30
        print(f"You have to guess a number between 1 to {end}")
        guessnum = random.randint(1, end)
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
        end = 60
        print(f"You have to guess a number between 1 to {end}")
        guessnum = random.randint(1, end)
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
        end = 100
        print(f"You have to guess a number between 1 to {end}")
        guessnum = random.randint(1, end)
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