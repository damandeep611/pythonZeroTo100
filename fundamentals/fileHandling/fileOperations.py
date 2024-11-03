from pathlib import Path
import pandas as pd

current_path  = Path.cwd()
print(f"Current working directory is: {current_path}")

# locating csv data file path
file_path = current_path.parent.parent / 'dataset' / 'hinduniliver.csv'
# verifying path before printing data - so first we will print the path 
print(f"-----csv file path: {file_path}")
#  and then using if else to only read the data if the file is found otherwise , error occurs 
if file_path.exists:
  print("CSV data file exits")
  df = pd.read_csv(file_path)
else:
  print("the requested file doesn't exits")



# stock analysis 
analysis = {
  'Highest Price': df['Close'].max(),
  'Lowest Price': df['Close'].min(),
  'Average Price': df['Close'].mean(),
  'Total Trading Days': len(df)
}
# writing results to a text file 
with open('hind_uni_results.txt', 'w') as file:
  for metric, value in analysis.items():
    file.write(f"{metric}: {value}\n")

# creating daily returns and create a new csv with this info
df['Daily_Returns'] = df['Close'].pct_change() * 100

# Write to a new csv file
df.to_csv('hind_uni_results.csv', index=False)

# calculate moving averages (20 day and 50 day) and exporting the results
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# exporting to excel file (more readable format)
df.to_excel('hind_uni_results.xlsx', index=False)

# finding specific patterns and writing them to a file

