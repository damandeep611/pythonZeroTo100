# basic dictionary operations 
student  = {
  "name": "Barry Allen",
  "age": 30,
  "skills": "Literally speed",
  "figths": [10, 20, 30]
}

print(student["skills"])

# adding updating items to dictionaries 
student["city"] = "Central City"
student["age"] = 31 # updating current value 

# some of the dictionary methods 
print(student.keys()) # get all keys
print(student.values()) # get all the values 
print(student.items()) # get all key value pairs


# checking if a key exits 
if "name" in student: 
  print("The 'name' key exits in student dict")


# get value with default if key doesn't exist
grade = student.get("score", 0) 
print(grade)