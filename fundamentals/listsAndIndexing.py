# lists are versatile data structures in python, to hold multiple items of different types.

#? first of all how to create a list 
stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "RL"]

# now that we have made the list we will start accessing the elements in the list , 

print(stocks[0])
print(stocks[2])
print(stocks[-1])
# -1 showed last item in the list because (-1 is negative indexing) and it starts from the last/end item of the list/array

# now that we have learned how to make a list and also how to access the elements of the list, so now we will Start to 

# ? modifying the lists

stocks.append("TSLA")   # to add an item to the list, in the end 
stocks.insert(1, "META") # to insert an item at a specific position
removed_stock = stocks.pop() #remove and return the last item

print(removed_stock) # returns the removed item from the list
print(stocks)

stocks.remove("GOOGL") #remove a specific item from list

# slicing in lists 
print(stocks[1:3]) # get a subset of the list