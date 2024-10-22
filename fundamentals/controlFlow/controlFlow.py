# control flow structures allow you to control the execution of your code based on conditions, as the x code will executed if it satifies a certain condition that is mentioned in the control flow statement 

# if else statements 

price = 100

if price > 100:
  print("The stock is expensive")
elif price < 50: 
  print("The stock is cheap")
else:
  print("The stock price is moderate")

# --------------------------------for loops -----------
  # looping through a list 

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN"]


for stock in stocks:
  print(stock)

# looping with range 
for i in range(5):
  print(i) # prints 0 to 4

# looping through a dictionary 

stock_prices = {
  "TATA": 100.60,
  "REL": 134.40,
  "ENGRY": 45.44,
}

for symbol, price in stock_prices.items():
  print(f"{symbol}: ${price}")


# -------------------While loops-----------------

# the following loop will keep adding +1 to 0 until i reaches 5 
counter = 0
while counter < 5:
  print(counter)
  counter += 1

