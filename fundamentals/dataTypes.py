# python data types 

#1. integers - whole numbers i.e 5, 10, -3, 0

x = 3
y= 10
j = -3
print(f"the three integers {x, y, j}")

#floting point numbers - decimal number 
a = 3.1459
b = -0.5
c = 2.0

#let's do some basic arithmatic operatiosn 
print(f"sum: {a + b}, product: {a * y}")

# and we already know string i.e 
thisOne = "hello world"
name = "python"
full_string = thisOne + " "  + name
print(full_string)

#and these are booleans to declare a value true or false 
tryThisOne = True

checkGreater = b > j
print(checkGreater)

#lists are ordered and are mutable collections 
numbers = [1,2,3,4,5,6,7,8]
numbers.append(12)
print(numbers)
# .append is one of many in built function that we use to operate some operations on lists 

#tuples - are ordered and are immutalbe collections 



# dictionaries are combo of key-value pairs, as there will be one key and a value will be assigned to this key, 

person = {
  "hero": "flash",
  "power": "superspeed",
  "universe": "DC",
  "age": 28
}

print(person)

#we can also person operations on this dictionaries i.e 
# to assign a new value 
person["multiverse"] = True
person["realName"] = "Barry Allen"
print(person)

