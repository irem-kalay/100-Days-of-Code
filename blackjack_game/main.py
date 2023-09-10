import random
from replit import clear
from art import logo

def calculate(list):
  if sum(list)== 21 and len(list) == 2: #The condition of blackjack represented.
    return 0
  total = 0
  for i in range(0, len(list)):
    total += list[i]
  if total > 21 and 11 in list:#changing "Ace" card from 11 to 1 value.
    find_index = list.index(11)
    list[find_index] = 1
    total = 0
    for i in range(0, len(list)):
      total += list[i]
  return total

def choose_random(list):#A function for choosing random card from list.
  random_card = random.choice(list)
  return random_card

def decide(player_sum, computer_sum):#A function to decide who is the winner.
  if player_sum > 21 and computer_sum > 21:
    print("You lose. You are over score 21.")
  elif player_sum > 21 and computer_sum <= 21:
    print("You lose. You are over score 21.")
  elif player_sum <= 21 and computer_sum > 21:
    print("You win.")

  elif player_sum <= 21 and computer_sum <= 21:
    if player_sum > computer_sum:
      print("You win.")
    elif player_sum < computer_sum:
      print("You lose.")
    elif player_sum == computer_sum:
      print("Draw.")
print(logo)
start = True
get_card = True
while start:
  want = input("Do you want to play Blackjack? 'yes' or 'no': ").lower()
  clear()
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player = []
  computer = []
  
  if want == 'yes':
    player.append(choose_random(cards))#both player and computer gets 2 cards at start of the game.
    player.append(choose_random(cards))
    computer.append(choose_random(cards))
    computer.append(choose_random(cards))
    score_player = calculate(player)
    score_computer = calculate(computer)
    if score_player == 0:
      print(" Blackjack, you win. ") #Blackjack condition.
      get_card = False #Not getting into while loop "Do you want to get another card?".
    print(f" Your cards are: {player}, current score: {score_player}.\n Computer's first card is: {computer[0]} \n")
    
    while get_card:
      another_card = input("Do you want to get another card? 'y' or 'n' to pass: ").lower()
      if another_card == 'y':
        player.append(choose_random(cards))
        computer.append(choose_random(cards))
        score_player = calculate(player)
        score_computer = calculate(computer)
        print(f" Your cards are: {player}, current score: {score_player}.\n Computer's first card is: {computer[0]} \n")
        if score_player > 21:
          print(f" Your final hand: {player}, final score: {score_player}\n Computer's final hand: {computer}, final score: {score_computer}\nYou lose ")
          break
      elif another_card == 'n':
        while score_computer < 17:
          computer.append(choose_random(cards))
          score_computer = calculate(computer)
        print(f" Your final hand: {player}, final score: {score_player}\n Computer's final hand: {computer}, final score: {score_computer} ")
        decide(score_player, score_computer)
        break
        
  if want == 'no':
    print("See you later.")
    start = False  
