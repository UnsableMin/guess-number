import random

print ("welcome to number Guesser")

comp_num = random.randint (0, 10)
tries = 3
won = False
play = True
while play == True:
  while tries > 0:
    print()
    player_num = input ("enter a number between 0-10:")
    player_num = float(player_num)
    if player_num < 0 or player_num > 10:
      print ("Bad Number")
      break
    else:
      if player_num == comp_num:
        print("correct")
        won = True
        print ("god level?")
        break
      elif player_num < comp_num:
        print("to small")
        tries -= 1
        print ("you have " + str(tries) + "tries left")
      else:
        print("to big")
        tries -= 1
        print ("you have " + str(tries) + ("left"))




