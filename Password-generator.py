#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#52 tane harf
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
nr_letters= int(input("How many letters do you want in your password?\n")) 
nr_symbols = int(input(f"How many symbols do you want?\n"))
nr_numbers = int(input(f"How many numbers do you want?\n"))

#easy level icin ayrica yapilabilecek 
# password =""
# for char in range(1, nr_numbers+1):
#  password += random.choice(letters)

cont_output = ""
count = 0
for letter in letters:
  if count < nr_letters:
    cont_output += str(letters[random.randint(0, len(letters) - 1)])
  count += 1


cont_output2 = ""
count2 = 0
for symbol in symbols:
  if count2 < nr_symbols:
    cont_output2 +=str(symbols[random.randint(0, len(symbols) - 1)])
  count2 += 1


cont_output3= ""
count3 = 0
for number in numbers:
  if count3 < nr_numbers:
    cont_output3 += str(numbers[random.randint(0, len(numbers) - 1)])
  count3 +=1

print(cont_output + cont_output2 + cont_output3)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = cont_output + cont_output2 + cont_output3

total_number_of_password = int(nr_letters)+int(+nr_symbols) +int(nr_numbers)

randomised_characters = random.sample(password, total_number_of_password)

togather = ""
count4 = 0
for character in randomised_characters:
  if count4 < total_number_of_password:
    togather += str(randomised_characters[count4])
  count4 += 1
print("Your new password might be: " + togather )