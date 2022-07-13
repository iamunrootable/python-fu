#Number Guessing Game Objectives:
import art
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def guess_number():
  print(art.logo)
  print("Welcome to Guess the number guessing game!\nI'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  
  # Verify difficulty is as expected
  difficulty_choices = ["easy","hard"]
  if difficulty not in difficulty_choices:
    print("Error: Incorrect difficulty level.")
  
  if difficulty == "easy":
    attempts = 10
  else: 
    attempts = 5
    
  secret_num = random.randint(1,100)
  
  game_over = False
  
  while not game_over:
    print(f"You have {attempts} remainig to guess the number")
    guess = int(input("Make a guess: "))
    
    if guess < secret_num:
      print("Too low")
      print("Guess again.")
    elif guess > secret_num:
      print("Too high")
      print("Guess again.")
    else:
      print(f"Your guess {guess} was the secret number: {secret_num}! You win!")
      game_over = True
      
    attempts -= 1
    
    if attempts < 1 and not game_over:
      game_over = True
      print("You have used all of your attempts and lost!")
  
  play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
  if play_again == 'y':
    guess_number()
  else:
    return

guess_number()