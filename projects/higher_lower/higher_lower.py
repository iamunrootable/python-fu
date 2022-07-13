import art
import game_data
import random
from replit import clear


def get_contestants():
  c_list = game_data.data
  i1 = random.randint(1,len(c_list) -1)
  i2 = random.randint(1,len(c_list) -1)

  a = c_list[i1]
  b = c_list[i2]
  
  
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  print(art.vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

  count_dict = {}
  count_dict['a'] = a['follower_count']
  count_dict['b'] = b['follower_count']
  
  return count_dict


def higher_lower():
  
  print(art.logo)
  
  score = 0
  game_over = False
  
  while not game_over:
    counts = get_contestants()
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if counts[choice] == counts['a']:
      score +=1
      clear()
      print(art.logo)
      print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True

  should_continue = input("Would you like to play again? Type 'y' or 'n': ").lower()
  if should_continue:
    clear()
    higher_lower()
  else:
    return      


higher_lower()