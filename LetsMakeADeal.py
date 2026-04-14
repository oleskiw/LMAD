#Explore: printing
print('Lets make a deal!')

#create the doors
doors = ['_', '_', '$']

#Randomize doors
import random
random.shuffle(doors)

#get some input
choice = eval(input('Choose a door (0,1,2): '))

#Challenge 2: determine which door to reveal
doors_to_reveal = [0,1,2]
if doors[0] == '$' or choice == 0:
  doors_to_reveal.remove(0)
if doors[1] == '$' or choice == 1:
  doors_to_reveal.remove(1)
if doors[2] == '$' or choice == 2:
  doors_to_reveal.remove(2)

reveal = random.sample(doors_to_reveal,1)

#Challenge 3: give player chance to switch doors
do_switch = input(f'You chose door {choice}. Door {reveal[0]} is empty.  Want to switch? (y/n): ')
if do_switch == 'n':
  choice_final = choice
else:
  options = [0,1,2]
  options.remove(reveal[0])
  options.remove(choice)
  choice_final = options[0]

print(f'You chose door {choice_final}.')

#Challenge 1: determine if the player won
if doors[choice_final] == '$':
  print('You won!')
else:
  print('You lose!')

print(f'The doors are: {doors}')
