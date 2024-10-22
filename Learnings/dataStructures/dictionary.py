# dictionary of stock prices 
# stock_prices = {"AAPL": 143.44, "GOOGL": 134.44, "TSLA": 700.12, "AMZN": 180.22}

# Basic dictionary operations
#Accessing values 
# apple_price = stock_prices["AAPL"]
# print(f"Apple inc, stock price is {apple_price}")

#adding a new stock
# stock_prices["MSFT"] = 420.53
# print(stock_prices)

#updating price of existing dictionary item
# stock_prices["GOOGL"] = 120.22
# print(stock_prices)

#removing stock item from the dictionary 
# del stock_prices["MSFT"]
# print(stock_prices)

# checking a stock exists in the dictionary 
# if "GOOGL" in stock_prices:
#   print("Google does exits in the demo dict")


# problem exercises 
# a portfolio tracking system 
portfolio = {
  "AAPL": {"shares": 10, "avg_price": 150.74},
  "GOOGL": {"shares":5, "avg_price": 140.50},
  "MSFT": {"shares": 8, "avg_price": 410.25}
}

# calculate total value of holdings 
current_prices = {
  "AAPL": 175.75,
  "GOOGL": 148.90,
  "MSFT": 420.25
}

total_value = 0
for stock, details in portfolio.items():
  shares  = details["shares"]
  current_price = current_prices[stock]
  stock_value = shares * current_price
  total_value += stock_value
  print(f"{stock}: {shares} shares worth ${stock_value:,.2f}")

print(f"Total portfolio Value: ${total_value:,.2f}")


