import random
from replit import clear

from hangman_word_turkish import kelime
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

user_language = input("Language Türkçe or English ? \n").lower()

if user_language == 'english':
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  end_of_game = False
  lives = 6
  display = []
  for _ in range(word_length):
      display += "_"

if user_language == 'türkçe':
  chosen_word= random.choice(kelime)
  word_length = len(chosen_word) 
  end_of_game = False
  lives = 6
  display = []
  for _ in range(word_length):
      display += "_"

  
while not end_of_game:
  if user_language == 'english':
    guess = input("Guess a letter: ").lower()
        
  elif user_language == 'türkçe':
    guess = input("Lütfen bir harf tahmin edin: ").lower()
        
  clear()  
      
  if guess in display:
    print("You already guessed this letter." if user_language == 'english' else "Bu harfi zaten tahmin etmiştiniz. ")

  for position in range(word_length):
    
    if guess == chosen_word[position]:
      display[position] = guess
      
  
    #Check if user is wrong.
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life." if user_language== 'english' else f"Kelimede olmayan {guess} harfini tahmin ettiniz ve bir hak kaybettiniz. ")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"You lose. The chosen word was : {chosen_word}" if user_language == 'english' else f"Kaybettiniz. Seçilen kelime {chosen_word} idi. ")

          #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

    #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win."if user_language == 'english' else "Kazandınız, tebrikler !")

  print(stages[lives])
