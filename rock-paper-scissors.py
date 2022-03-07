# rock-paper-scissors.py
import random

choices = ['rock', 'paper', 'scissors']
botIn = random.choice(choices)

userIn = input('Rock, paper, scissors!')
if userIn == botIn:
  print('tie!')
elif userIn == choices[0]:
  if botIn == choices[1]:
    print('you lose! the bot chose paper.')
  elif botIn == choices[2]:
    print('you win! the bot chose scissors.')
elif userIn == choices[1]:
  if botIn == choices[0]:
    print('you win! the bot chose rock.')
  elif botIn == choices[2]:
    print('you lose! the bot chose scissors.')
elif userIn == choices[2]:
  if botIn == choices[0]:
    print('you lose! the bot chose rock.')
  elif botIn == choices[1]:
    print('you win! the bot chose paper.')

print('thanks for playing!')
