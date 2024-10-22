from pathlib import Path
import pandas as pd

# importing csv file using pathlib , and printing current file path
current_dir = Path.cwd()
print(f"Current working dir: {current_dir}")

# going up two levels for csv file 
file_path = current_dir.parent.parent / 'dataset' / 'ADANIPORTS.csv'
df = pd.read_csv(file_path)


# method 2 - to use relative path directly 

df = pd.read_csv('../../dataset/ADANIPORTS.csv')
print(df.head())

# ? if the csv file was in the same directory/folder then we would have used this method 
df = pd.read_csv('stockdata.csv')

# how to verify path before reading 

# first print the constructed path to check if it's correct 
print(f"File path: {file_path}")

#check if the file exists 
if file_path.exists():
  print("File found!")
  df = pd.read_csv(file_path)
  print(df.head()) # show first 5 rows
else:
  print("File not found. Please check the path")
