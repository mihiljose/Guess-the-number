import random
from art import logo

print(logo)

print("Welcome to the number Guessing Game! \nI'm Thinking of a number between 1 and 100")

random_no = random.randint(1,100)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level.lower() == "easy":
    attempts = 10
    print("You have 10 Attempts")
else:
    attempts = 5
    print("You have 5 Attempts")
while attempts!=0:
    guess = int(input("Make a guess: "))
    if guess>random_no:
        print("Too high!\nGuess Again😁")
        attempts-=1
        if attempts ==0:
          print("You have run out of guesses! game Over!")
        else:
          print(f"You have {attempts} attempts remaining")

    elif guess<random_no:
        print("Too Low!\nGuess Again😁")
        attempts-=1
        if attempts ==0:
          print("You have run out of guesses! game Over!")
        else:
          print(f"You have {attempts} attempts remaining")

    else:
        print("You guessed it right!😃")
        attempts = 0
