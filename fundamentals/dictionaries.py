# dictonaries store key value pairs and are very useful for representing structured data.

stock_prices = {
  "AAPL": 150.25,
  "GOOGL": 2750.50,
  "MSFT": 305.75
  }

# accessing and modifying values in the dictionaries 
print(stock_prices["AAPL"])


stock_prices["TSLA"] = 800.00 # adding a new key value pair in the existing dictionary
stock_prices["AAPL"] = 145.40 # modifying existing value of a key

print(stock_prices)

# checking if a key exists 

if "AMZN" in stock_prices: 
  print(stock_prices["AMZN"])
else: 
  print("AMZN not found in the dictionary")