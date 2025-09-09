import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("🔼 Too low! Try again.")
            elif guess > number:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
