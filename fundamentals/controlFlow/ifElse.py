# if else is a simple, do this if this happens and if this doesn't happen execute this, so simply put it's a control structure statements in our code to perform tasks when certain conditions are met, 

# age = 20

# if age > 18:
#   print("you are a adult")
# else:
#   print("you are a minor")

# multiple conditions using elif

score = 95

if score >= 90:
  print("A Grade")
elif score >= 80:
  print("B Grade")
elif score >= 70:
  print("C Grade")
elif score >= 60:
  print("D Grade")
else:
  print("F Grade")


# nested if else statements 

is_weekday = True
is_holiday = False
weekday_holiday = True

if is_weekday:
  if is_holiday:
    print("it's a holiday ! no work today")
  elif weekday_holiday:
    print("no holiday on weekday, go to work")
  else:
    print("Time to go to work.")
else:
  print("it's the weekend! relax")


# using logical operators (and, or)

temprature = 45
is_sunny = True
superhot_sun = True

if temprature < 25 and is_sunny:
  print("it's the perfect day for the beach")
elif temprature < 30 and superhot_sun:
  print("it's nice day , but not ideal for the beach")
elif temprature > 40 and  is_sunny:
  print("It's gonna be fcking scorched earth out there, so let's sty intoors")
else:
  print("Maybe stay indoors today")


  # some problems to solve for if else 
def is_even_or_odd(num):
  if num % 2 == 0:
    print("even number")
  else:
    print("odd number")

is_even_or_odd(11)
is_even_or_odd(12)

# if else to check if a person if old enough to vote 
def ageCheck(age):
  if age > 18:
    print("you are eligible to vote")
  elif age < 18:
    print("you are just a noob still")
  else:
    print("democracy is a sham kid don't vote")
ageCheck(18)
ageCheck(49)
# if else to check if a number is within a certain limit range 

def checkNumLimit(num, max_limit, min_limit):
  if max_limit > num > min_limit:
    print("the number is within the permissible limit")
  else:
    print("the number is not what i expected")
checkNumLimit(7, 10, 3)

# to check if user has entered a valid password, as the valid password has 8 words limit
EnterPassword = input("Enter you password to check it's strength: ")

if len(EnterPassword) >= 8:
  print("Your password has valid length")
else:
  print("you password is weak bitch")

