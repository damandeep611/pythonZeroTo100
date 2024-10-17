import matplotlib.pyplot as plt # to import functions for creating plots
import pandas as pd # pandas for data structures and functions for data analysis
import numpy as np # numpy for numerical computing

# simple dataset with stock prices

np.random.seed(0)
dates = pd.date_range('2022-01-01', '2022-12-31')
prices = np.random.normal(100,20, size=len(dates))

df = pd.DataFrame({'Date': dates, 'Price': prices})

plt.figure(figsize=(12,6))

plt.plot(df['Date'], df['Price'])

plt.title('Stock prices over time')

plt.xlabel('Date')

plt.ylabel('Price')

plt.grid(True)

plt.show()
