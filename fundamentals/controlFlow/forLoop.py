# basic for loop through a range 
for i in range(1):
  print(i)

# loop with range starting and ending points
for i in range(2,6):
  print(i)

# looping through a list 
characters = ['batman', 'flash', 'superman', 'shazam', 'martian']
for heros in characters:
  print(heros)

#loop with step value 
# the third value in the range is the count jump, as if.. if  it was 3 the count would go from 0 to 3 and then 6 and so on

for i in range(0, 10, 2):
  print(i)

# looping through a string 
print("looping through a string")


string_loop_test = "ApplesBud"

for char in string_loop_test:
  print(char)

# counting the number of vowels in a string

vowel_count = 0
for char in string_loop_test:
  if char in 'aeiou':
    vowel_count += 1
print(f"Number of vowels in given string is : {vowel_count}")

# reversing a string

reversed_string = ""
for char in string_loop_test:
  reversed_string = char +  reversed_string
print(reversed_string)

# loop that prints all even number from 1 to 20
for i in range(20):
  if(i % 2 == 0):
    print(i)

# create a list of numbers from 1 to 10, then write a loop that prints the square of each number
num_List = [1,2,3,4,5,6,7,8,9,10]

# for i, v in enumerate(num_List):
#   num_List[i] = v**2
# print(f"Square elements: {num_List}")


# the above method is to modify the original list, but to print square of each number without modification to original list we can use 
for num in num_List: 
  print("square of num in list",num ** 2) 


# loop to create a pattern 
for i in range(6):
  print(i * "*") 

#pattern to right side now
for i in range(6):
  spaces  = " " * (5 - i)
  stars = "*" * (i + 1)
  print(spaces + stars)

# method 2 for right side pattern
for i in range(1,6):
  print(("*" * i).rjust(5 ))

  # Problem 5 - Number pattern
for i in range(1, 6):
    print(str(i) * i)

# Problem 6 - Pyramid pattern
# Method 1: Using string multiplication
for i in range(5):
    spaces = " " * (4 - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# Method 2: Using center() string method
for i in range(5):
    stars = "*" * (2 * i + 1)
    print(stars.center(9))


