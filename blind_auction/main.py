from replit import clear
from art import logo
print(logo)

again = True
name_and_value = {}
print("Welcome to blind auction! \n ")

while again :
  name = input("What is your name? ")
  bid_price = input("How much is your bid price? ")

  #creating a dictionary
  name_and_value[name] = bid_price
  #if there are more people, clear the page & restart
  more_people = input("Are there more user? (Yes or No) ").lower()
  clear()
  
  if more_people == 'no':
    again = False
# I placed the names and bids in 2 different list from library and then compared bids and selected winner name by index 
list=[]
names=[]
for key in name_and_value: 
  number = int(name_and_value[key])
  list.append(number)
  names.append(key)

highest = max(list)
index_of_highest = list.index(highest)

highest_numbers_count = list.count(highest)
#check if there are more than 1 highest number
if highest_numbers_count >= 2:
  print(f"There is no winner. Try again. Some people guessed the same biggest number : {highest}. ")
  
if highest_numbers_count < 2:    
  print(f"The winner of the blind auction is {names[index_of_highest].upper()} with {list[index_of_highest]}, Congratulations! ")
# to emphasis the name of winner, I made all letters of the name upper case