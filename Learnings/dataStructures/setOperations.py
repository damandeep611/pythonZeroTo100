# set operations 
#? Set operations in Python allow you to perform mathematical operations on sets, such as union, intersection, difference, and symmetric difference. These operations are useful for tasks like finding common elements, unique elements, or combining sets.

# creating sets 
marvel = {"spiderman", "ironman", "wolverine", "movies"}
dc  = {"batman", "superman", "flash", "movies"}

# set operations 
union = marvel | dc  # adding all elements from both sides is union
intersection = marvel & dc # adding common elements from both sides
difference = marvel - dc # elements in marvel but not in dc
symmetric_diff = marvel ^ dc # elements in either set, but not both

print(union, intersection, difference, symmetric_diff)


# ? Adding and removing elements 
marvel.add("doctor") # add a single element 
marvel.remove("wolverine") # remove element 
marvel.discard("movies") # remove element

# check membership 
if "spiderman" in marvel:
  print("Spiderman is in Marvel")


# understanding set operations in the context of stock market 
nasdaq_stocks = {"AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"}
sp500_stocks = {"AAPL", "MSFT", "JPM", "BAC", "WMT"}

# do set operations in context of these set operations 

# problem  - Sector Analysis  - using set operations methods
# creating set of stocks by sector 
tech_stocks = {"AAPL", "GOOGL", "MSFT", "AMZN"}
finance_stocks = {"JPM", "BAC", "GS", "MS"}
retail_stocks = {"WMT", "AMZN", "TGT", "COST"}

#finding stocks that are in both tech and retail 
tech_retail = tech_stocks.intersection(retail_stocks)
print(f"Companies in both tech and retail are: {tech_retail}")

# all unique stocks across sectors 
all_sector_stocks = tech_stocks.union(finance_stocks).union(retail_stocks)
print(f"Total unique stocks tracked: {all_sector_stocks}")