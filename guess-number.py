import random
from art import logo

print(logo)

print("Welcome to the number Guessing Game! \nI'm Thinking of a number between 1 and 100")

random_no = random.randint(1,100)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level.lower() == "easy":
    attempts = 10
else:
    attempts = 5
    
while attempts!=0:
    guess = int(input("Make a guess: "))
    if guess>random_no:
        print("Too high!\nGuess Again")
    elif guess<random_no:
        print("Too Low!\nGuess Again")
    else:
        print("You guessed it right!")
        attempts = 0
