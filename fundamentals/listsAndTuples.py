# lists and tuples in python and key differences 

#lists are mutable as we can change them after assigning values to them i.e

performers = ["test", "hero", "slicer", "cutter"] 
performers[0] = "villan"
performers.append("neutral")
print(performers)

# why lists are used 
  # when we need to frequently add, remove or modify the elements in the lists i. e a todo list application 
  # or when storing data of current users that might keep changing

todo_list = ["hiking App", "Trading App", "python trade"]
todo_list.append("portfolio website")
todo_list.remove("python trade")

print(todo_list)





# tuples are immutable as we can't change their assigned value after creating it
cordinates = (89.81, 45.89)
## cordinates[0] = 99  this will throw errors 
print(cordinates)

#trying to modify a tuple 
try:
  cordinates[1] = 120
except TypeError as e:
  print(f"Error while modifying tuple is : {e}")

# when we are working with data that sholdn't be changes that 's when we use tuples , i.e data that contains cordinates etc 

# tuples can also be used as dictonaries key , because they're immutable 

locations = {
  (40.7128, 74.0060): "New York City",
  (34.0522, 118.2437): "Los Angeles"
}
# so to keep it short, we used tuples when we don't want the data to be changed accidently and that migth be the user information or some sensitive data that you have stored on your storage





