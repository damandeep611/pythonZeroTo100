# pyhon uses dynamic typing so we don't need to explicitly declare the type of the variable, but we can if we want to by using type hints for example:
# name: str = "Alice" 

name = "Alice"
age = 30
price = 99.99890
is_trading = True

print(f"Hello {name}, you are {age} years old and the price is {price:.2f} and is trading {is_trading}")

# the f is for format string and it allows us to embed the variables inside the string, we can also format the price to 2 decimal places by using {price:.2f}, we can also use the round function to round the price to 2 decimal places by using round(price, 2)
print(f"Hello {name}, you are {age} years old and the price is {round(price, 2)} and is trading {is_trading}")  
