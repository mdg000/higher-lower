# 100 Days of Code 
# Higher or Lower

import random
from replit import clear
from art import logo, vs
from game_data import data

#game variables
game_continue = True
score = 0
loop = 0
winner = 0

top = random.randint(1, len(data))
bottom = random.randint(1, len(data))
# game loop
while game_continue:

  print(logo)

  if loop != 0:
    print(f"You're right! Current score: {score}")
    top = winner
    bottom = random.randint(1, len(data))
  # main game screen
  print(f"Compare A: {data[top]['name']}, a {data[top]['description']}, from {data[top]['country']}.")
  print(vs)
  print(f"Against B: {data[bottom]['name']}, a {data[bottom]['description']}, from {data[bottom]['country']}.")

  user_guess = (input("Who has more followers? Type 'a' or 'b': "))

  # game and scoring logic
  wrong = False
  if user_guess == 'a':
    if data[top]['follower_count'] > data[bottom]['follower_count']:
      score += 1
      winner = top
    else:
      wrong = True
  elif user_guess == 'b':
    if data[bottom]['follower_count'] > data[top]['follower_count']:
      score += 1
      winner = bottom
    else:
      wrong = True

  loop += 1

  clear()
  
  # game over
  if wrong:
      print(logo) 
      game_continue = False
      print(f"Sorry, that's wrong. Final Score: {score}")