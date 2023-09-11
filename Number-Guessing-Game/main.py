import random
from replit import clear
from ascii_art import ascii

game_start = True

def deciding(random_number, guessing): #A function for comparing numbers.
  if random_number < guessing:
    print(" Too high.\nGuess again.\n")
  elif random_number > guessing:
    print(" Too low.\nGuess again.\n ")
  elif random_number == guessing:
    print(" Congratulations, You Win! \n")

def ask():
  again = input("Do you want to play again? 'yes' or 'no'? ").lower()
  if again == 'yes':
    global game_start
    game_start = True
    clear()
    print(ascii)
  elif again == 'no':
    game_start = False
    print("See you! ") #Asking if player wants to play one more time
print(ascii)    
print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")

while game_start:
  difficulty = input(" Choose a difficulty. Type 'easy' or 'hard'? ").lower()

  selected_number = random.randint(1, 100) #choose a number between 1 and 100.

  easy_attempt = 10
  hard_attempt = 5
  while easy_attempt != 0 or hard_attempt != 0:
    if difficulty == "easy":
      print(f"You have {easy_attempt} remaining to guess the number.")
      easy_attempt -= 1
    elif difficulty== "hard":
      print(f"You have {hard_attempt} remaining to guess the number.")
      hard_attempt -= 1
    guess = int(input(" Make a guess: "))
    deciding(selected_number, guess)
    if selected_number == guess:
      easy_attempt = 0
      hard_attempt = 0
      ask() #asking player wheather want to play again.
    elif easy_attempt == 0 or hard_attempt == 0:
      print(f"You lost. You have 0 attempts. The number was {selected_number}. ")
      easy_attempt = False 
      hard_attempt = False
      ask()  