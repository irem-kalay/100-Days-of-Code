rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock, paper, scissors]

user_number = int(input("Enter a number for Rock, Paper and Scissors. (Rock = 0, Paper = 1, Scissors = 2) \n"))

print(game[(user_number)])

computer_random_number = random.randint(0, 2)
print("Computer chose: \n " + game[computer_random_number])

if user_number==0 and computer_random_number == 0:
  print("Draw")

if user_number==0 and computer_random_number == 1:
  print("You lost!")

if user_number==0 and computer_random_number == 2:
  print("Congratulations, you won!")

if user_number==1 and computer_random_number == 0:
  print("Congratulations, you won!")
if user_number==1 and computer_random_number == 1:
  print("Draw")
if user_number==1 and computer_random_number == 2:
  print("You lost!")

if user_number==2 and computer_random_number == 0:
  print("You lost!")
if user_number==2 and computer_random_number == 1:
  print("Congratulations, you won!")
if user_number==2 and computer_random_number == 2:
  print("Draw")