## indentation in python 

def outer_function():
  if True:
    print("first level")
    for i in range(3):
      print("Second level")
      if i == 2:
        print("Third level")

  
# the outer_function is the correct indentation style as providing space before the line will keep on increasing as the function wraps more function inside 

# common beginner mistake is - inconsistent indentation 
def wrong_function():
  print("First Line")
print("wrong indent") # may cause indentation error 


