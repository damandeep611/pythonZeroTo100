# most used loops in data analysis  are for loop and while loop and nested loops so first master this 

#? for loops
# for loops are used to iterate through multiple number of items
#basic for loop through a list 


# characters = ['batman', 'flash', 'superman', 'shazam', 'martian']
# for heros in characters:
#   print(heros)

# for loop using range for looping through numbers

# for i in range(3):
#   print(i)


#? while loop - it will keeep on running while the condition you provided is true

# basic while loop
# num = 0
# while num < 5:
#   print(num)
#   num += 1

# while loop with a break 

# while True:
#   user_input = input("Enter 'quit' to exit the CLI: ")
#   if user_input == 'quit':
#     break

#? Nested Loops  - loops inside loops 
# for i in range(3):
#   for j in range(2):
#     print(f"i: {i}, j: {j}")


# ? some imp loop control statements to remember - write another md file for it 

# break - to exit the loop 
for i in range(4):
  if i == 3:
    break # it will stop at 3 and not go further till 4
  print(i)

# continue - to skip a step in the loop
for j in range(4):
  if j == 2:
    continue
  print(j)

# else with loops  - executes when loop completes normally 
for i in range(3):
  print(i)
else:
  print("LOop completed")