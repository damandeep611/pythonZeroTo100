# day one exercise will be calculating compound interest using variables and operations 

#formula to calculate compound interest annually is given by 
# A = P(1 + R/100)t  - here A = amount , and P = principle
# compound interest =  amount - principle 
#using a function 
def Calculate_compound_interest(principle, rate, time):
  Amount = principle * (pow((1 + rate/100), time))
  CI = Amount - principle
  print("Compound interest is:", CI)

Calculate_compound_interest(10000, 10.25, 5)


