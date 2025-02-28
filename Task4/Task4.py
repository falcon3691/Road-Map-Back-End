import random
import os
def tahmin_oyunu():
    os.system("cls")
    selectedNumber = random.randint(1, 100)  # 1 ile 100 arasında rastgele sayı seç
    guessNumber = 0
    
    print("-"*50)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    print("Please select the difficulty level:\n" +
          "1. Easy (10 chances)\n" +
          "2. Medium (5 chances)\n" +
          "3. Hard (3 chances)\n" +
          "4. Exit")
    diff = int(input("Enter your choice: "))
    
    if diff == 1:
        chances = 10
    elif diff == 2:
        chances = 5
    elif diff == 3:
        chances = 3
    elif diff == 4:
        return 0
    print("\nGame Started")
    print("-"*50)
    while diff:
        try:
            if guessNumber < chances:
                guess = int(input("Enter your guess: "))
                guessNumber += 1
                
                if guess < selectedNumber:
                    print(f"Incorrect! The number is greater than {guess}")
                elif guess > selectedNumber:
                    print(f"Incorrect! The number is less than {guess}")
                else:
                    print("-"*50)
                    print(f"Congratulations! You guessed the correct number in {guessNumber} attempts.")
                    diff = int(input("Do you want to play again Yes(1) / No(2): "))
                    if diff == 1:
                        break
                    elif diff == 2:
                        return 0
                    
            else:
                print("-"*50)
                print(f"Game Over! The number was {selectedNumber}")
                diff = int(input("Do you want to play again Yes(1) / No(2): "))
                if diff == 1:
                    break
                elif diff == 2:
                    return 0
        except ValueError:
            print(f"Please enter a number!")
    return 1

while tahmin_oyunu():
    continue
