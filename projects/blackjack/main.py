import random
import art

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(list):
  #global user_score, computer_score
  score  = sum(list)

  if score == 21 and len(list) == 2:
    score = 0
    
  if score > 21 and 11 in list:
    i = list.index(11)
    list[i] = 1
    calculate_score(list)
    
  return score

def compare(u_score,c_score):

  if u_score == c_score:
    return "Draw 🙃"
  elif u_score == 0:
    return "Win with a Blackjack 😎"
  elif c_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif u_score > 21:
    return "You went over. You lose 😭"
  elif c_score > 21:
    return "Opponent went over. You win 😁"
  elif u_score > c_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def blackjack():
  user_cards = []
  computer_cards = [] 
  print(art.logo)
  game_over = False
# First Hand
  while not game_over:
    for c in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    
    user_score =  calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    if user_score != 0 and computer_score != 0:
      print(f"Your cards: {user_cards}, current score: {user_score}\nDealer's first card: {user_cards[1]}")
      hit_me = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    else: 
      print(compare(user_score,computer_score))
      game_over = True
    
    if hit_me == "y":
      user_cards.append(deal_card())
      user_score =  calculate_score(user_cards)
      if user_score == 21:
        while computer_score < 17 and computer_score != 21 and computer_score < 21:
          computer_cards.append(deal_card())
          computer_score = calculate_score(computer_cards)
        print(compare(user_score,computer_score))
        hit_me = "n"
        game_over = True
      elif user_score > 21:
        print(f"Your final cards: {user_cards}, final score: {user_score}\nDealer's first card: {user_cards[1]}")
        print(compare(user_score, computer_score))
        hit_me = "n"
        game_over = True
      else:
        print(f"Your cards: {user_cards}, current score: {user_score}\nDealer's first card: {user_cards[1]}")
        hit_me = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    else:
      while computer_score < 17 and computer_score != 21 and computer_score < 21:
          computer_cards.append(deal_card())
          computer_score = calculate_score(computer_cards)
      print(f"Your final cards: {user_cards}, final score: {user_score}\nDealer's cards: {computer_cards}")
      print(compare(user_score,computer_score))
      game_over = True
  play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
  if play_again == "y":
    blackjack()

  
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play_game == "y":
  blackjack()

