age = 14

if age > 18:
  print("you are a adult")
else:
  print("you are a minor")

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
