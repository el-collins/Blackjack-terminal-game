from art import logo
import random
from replit import clear
def deal_card():
  """Return random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(hand):
  
  if sum(hand) == 21 and len(hand) == 2:
    return 0

  if sum(hand) > 21 and 11 in hand:
    hand.remove(11)
    hand.append(1)
    
  return sum(hand)

def compare(user_score, computer_score):
  if computer_score ==  user_score:
    return "It's a Draw"
  elif computer_score == 0:
    return "Lose,  opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Oppenent went over. You win!"
  elif computer_score > user_score:
    return "Computer wins"
  else:
    return "You win"




def play_game():
  # clear()
  
  
  user_cards = []
  computer_cards = []
  is_end_game = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  # print(logo)
  
  # print(user_cards, computer_cards)
  while not is_end_game:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_end_game = True
    else:
      should_user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if should_user_deal == 'y':
        user_cards.append(deal_card())
        # calculate_score(user_cards)
      else:
        is_end_game = True
        play_game = "n"
        
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  
  play_game()
