import random
import os
import sys
import time

os.system('clear')
print("    **** Welcome to Hangman game ****    ")

name = input("Enter your Name : ")
print(f'   Welcome {name}!')

def quit():
  os.system('clear')
  print(f' *** Result ***')
  print(f'{name}, Your score: {user_score}')
  sys.exit(f" *** Thankyou for playing {name}! ***")


#initial value
user_score = 0
tries = 0
initial_word_count = 0


#read words.txt file
with open('words.txt','r') as f:
  words = list(f)

try:
  total_words = int(input("How many words you want to play with : "))
  max_tries = int(input("How many chances you need to try : "))
except ValueError:
  print(' *** ERROR ***')
  print("Enter an integer value...")
  raise

def hangman():
  word = list(random.choice(words).strip())
  guess = list('*' * len(word))
  print(f' Guess the Word :{guess}')
  global tries,total_words,max_tries,user_score,initial_word_count
  

  while tries in range(max_tries):
    print(f'        Chances : {tries+1} out of {max_tries}')
    User_guess = list(input('Enter your Guess word : '))

    if User_guess == word:
      print("You got it, Congratz!!!")
      user_score += 1
      initial_word_count +=1
      main()
    elif User_guess != word:
      print("Wrong, Try Again")
      tries += 1
      #end of while loop

  print(f' Random Word : {word}')
  time.sleep(3)
  quit()

#main pgm
def main():
  if initial_word_count in range(total_words):
    hangman()
  else:
    quit()

main()
