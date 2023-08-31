#There is 2 alphabet inside the list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  if shift_amount > 26 :  #To prevent the bug when user entered the shift number more than 26
    shift_amount= shift_amount % 26 # % 26 because there are 26 letters in the alphabet
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1 #while decoding shift amount goes backwards
  for char in start_text:  
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]        
    else:
      end_text += char #if char is not in the alphabet, it is written at the end how it is
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)


program_continue = True
while program_continue:  
  direction = input("Type 'encode' to encrypt, type 'decode' to     decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  #asking the user if he wants to work the program again
  stop_or_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  if stop_or_continue == "yes" :
    program_continue= True
    
  else:
    print("Goodbye")
    program_continue = False
