# common loop patterns to practice 

# looping through sequence with index

colors = ['red', 'blue', 'green', 'yellow']
for index in range(len(colors)):
  print(f"index {index}: {colors[index]}")

# better way to use enumerate ()
for haha, bitch in enumerate(colors):
  print(f"index {haha}: {bitch}")

# looping through dictionaries 
  person = {'name': 'john', 'age': 30}
  for key in person:
    print(f"{key}: {person[key]}")

# better way to loop through dictionaries
for key, value in person.items():
  print(f"{key}: {value}")


# Practice exercises you can try:

# Write a loop to print numbers 1-10
# Sum all numbers in a list using a loop
# Find the largest number in a list using a loop
# Create a multiplication table using nested loops