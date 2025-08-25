def show_levels():
  print('Game levels:')
  print()
  print('(1) Easy\n * limits:[1 - 10]\n *No, of trials : 3')
  print()
  print('(2) Intermediate\n limits:[1 - 100]\n *No, of trials : 7')
  print()
  print('(3) Hard\n limits:[1 - 1000]\n *No, of trials :10 ')
show_levels()

def game_level_choice():
       game_level = input('choose the level you want to play\n:')
       return game_level


def set_game_settings(game_level):
  if game_level == '1':
    limits = range(1, 11)
    n_trials = 3
  elif game_level == '2':
    limits = range(1, 101)
    n_trials = 7
  elif game_level == '3':
    limits = range(1,100)
    n_trials = 15
  return limits, n_trials

import random

def start_play(limits, n_trials):
  number = random.choice(limits)
  guss = int(input(f'guess the number between {limits}:'))
  user_trials = 1
  while user_trials < n_trials:
    if guss == number:
      print(f'Congratulations, you achieved it in {user_trials} trial')
      break
    elif guss < number:
      print('Increase')
      guss = int(input(f'guess the number between {limits}:'))
      user_trials += 1
    elif guss > number:
      print('Decrease')
      guss = int(input(f'guess the number between {limits}:'))
      user_trials += 1
  else:
    print('You Lose!')

def play():
  show_levels()
  game_level = game_level_choice()
  limits, n_trials = set_game_settings(game_level)
  start_play(limits, n_trials)

play()