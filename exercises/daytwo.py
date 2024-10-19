# Create a list of stock prices and calculate the average

stock_prices = [145.23, 142.50, 147.80, 144.90, 143.75, 146.80]

# calculate the average 
def calculate_average(prices):
  if not prices:
    return 0
  return sum(prices) /len(prices)

result = calculate_average(stock_prices)
print(result)


# a program to calculate real time analysis of values 
def analyze_stock_prices():
  stock_rates = []

  print("Stock price analysis program")
  print("Enter Stock prices (enter 'done' when finished)")

  while True:
    user_input = input("Enter stock price: ")

    if user_input.lower() == 'done':
      break

    try:
      price = float(user_input)
      if price < 0:
        print("Pleaes enter a valid positive number")
        continue
      stock_rates.append(price)

      #show current stats 
      print(f"\nCurrent stock prices: {stock_rates}")
      print(f"Current average: ${calculate_average(stock_prices):.2f}")
      print(f"Highest price: ${max(stock_prices):.2f}")
      print(f"Lowest price:")

    except ValueError:
      print("Invalid input ! Please enter a valid number")

    if stock_rates:
      print("\nFinal Analysis:")
      print("-" * 20)
      print(f"Number of prices entered: {len(stock_rates)}")
      print(f"Average price: ${calculate_average(stock_rates):.2f}")
      print(f"Highest price: ${max(stock_rates):.2f}")
      print(f"Lowest price: ${min(stock_rates):.2f}")

analyze_stock_prices()