from game_data import data
from replit import clear
import random
from ascii_art import logo_higher_lower, vs

#Choose random number
def random_number(list):
  number = random.randint(1, len(list) - 1)
  return number
#Makes the informations about celebrity a list.
def information(data):
  number = random_number(data)
  dictionary = data[number]
  info = []
  for celebrity_info in dictionary:
    info.append(dictionary[celebrity_info])
  return info
  
info = information(data)
info2 = information(data)
print(logo_higher_lower)
print(f"\nCompare A: {info[0]}, a {info[2]}, from {info[3]}.")
print(vs)
print(f"\nAgainst B: {info2[0]}, a {info2[2]}, from {info2[3]}.")
choose = input("Who has more followers? Type 'A' or 'B':").upper()
clear()
# The followers counts
follower = int(info[1])
follower2 = int(info2[1])

score = 0
while choose == 'A' or choose == 'B':
  print(logo_higher_lower)
  if choose == 'A':
    if follower > follower2:
      score += 1
      print(f"\nYou're right! Current score: {score}.")
      print(f"Compare A: {info2[0]}, a {info2[2]}, from {info2[3]}.")
    elif follower < follower2:
      print(f"Sorry, that's wrong. Final score: {score}")
      break
      
  if choose == 'B':
    if follower2 > follower:
      score += 1
      print(f"\nYou're right! Current score: {score}.")
      print(f"Compare A: {info2[0]}, a {info2[2]}, from {info2[3]}.")
    elif follower2 < follower:
      print(f"Sorry, that's wrong. Final score: {score}")
      break
    # Making B into A. (unindent and not inside if blocks but iinside the while loop.)
  info = info2
  follower = follower2 
    #Choosing new celebrity.
  info2 = information(data)
  follower2 = int(info2[1])
  print(vs)
  print(f"Against B: {info2[0]}, a {info2[2]}, from {info2[3]}.")
  choose = input("Who has more followers? Type 'A' or 'B':").upper()
  clear()   