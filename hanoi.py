from stacknode import *

print("\n/-\ TOWERS OF HANOI /_\\")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to use?\n"))
while num_disks<3:
  num_disks =int(input("You need >= 3 disks.\n"))
  
for x in range(num_disks,0, -1):
  left_stack.push(x)

num_optimal_moves = 2**num_disks - 1
print("\n{0} is the optimal number of moves".format(num_optimal_moves))
#Get User Input
def get_input():
  choices = [x.get_name()[0] for x in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("{0} : {1}".format(letter, name))
    user_input = input("")
    print(user_input)
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
          break
        
#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for i in range(len(stacks)):
    stacks[i].print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    
    if from_stack.peek() == None:
      print("\n\nInvalid Move. Try Again")
    elif to_stack.peek() == None or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
 
  print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
  
